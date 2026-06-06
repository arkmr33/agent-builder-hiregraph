from hiregraph.nodes.rejection import rejection_check
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import RetryPolicy
from langgraph.prebuilt import ToolNode
from src.hiregraph.state import HireGraphState
from src.hiregraph.ingest import ingest_resume_and_jd
from src.hiregraph.nodes.classify import classify_seniority
from src.hiregraph.nodes.planning import plan_required_skills, wait_for_all
from src.hiregraph.nodes.orchestrator import assign_skill_workers
from src.hiregraph.nodes.skillworker import skill_worker
from src.hiregraph.nodes.scoring import (
    experience_scorer,
    education_scorer,
    signal_scorer,
    aggregate_scores
)
from src.hiregraph.nodes.recovery import parser_node, parser_router, repair_node
from langgraph.prebuilt import tools_condition
from src.hiregraph.nodes.research_agent import research_agent
from src.hiregraph.nodes.toolnode import *
from src.hiregraph.nodes.decision import recommendation
from src.hiregraph.nodes.routes import (
    advance,
    reject,
    borderline
)
from src.hiregraph.nodes.human_review import human_review
from src.hiregraph.nodes.email import (
    draft_email,
    critic_loop,
    send_email_and_update_ats
)
from src.hiregraph.nodes.rejection import (
    draft_rejection,
    log_rejection
)
from src.hiregraph.nodes.compensation import compensate
from src.hiregraph.nodes.finalize import finalize, saver
from src.hiregraph.nodes.saga_router import ats_result_router


def build_graph():

    builder = StateGraph(HireGraphState)

    # ==================================================
    # TOOL NODE
    # ==================================================

    # tool_node = ToolNode([
    #     tavily_search,
    #     github_lookup
    # ])

    builder.add_node("tool_node", debug_tool_node)



    # ==================================================
    # CORE PIPELINE
    # ==================================================

    builder.add_node(
        "ingest_resume_and_jd",
        ingest_resume_and_jd
    )

    builder.set_entry_point("ingest_resume_and_jd")

    builder.add_node(
        "classify_seniority",
        classify_seniority
    )

    builder.add_node(
        "plan_required_skills",
        plan_required_skills
    )

    # ==================================================
    # ORCHESTRATOR + WORKERS
    # ==================================================

    builder.add_node(
        "skill_worker",
        skill_worker
    )

    # ==================================================
    # SCORERS
    # ==================================================

    builder.add_node(
        "experience_scorer",
        experience_scorer
    )

    builder.add_node(
        "education_scorer",
        education_scorer
    )

    builder.add_node(
        "signal_scorer",
        signal_scorer
    )

    builder.add_node(
        "aggregate_scores",
        aggregate_scores
    )

    builder.add_node(
    "wait_for_all",
    wait_for_all
)

    # ==================================================
    # RESEARCH AGENT
    # ==================================================

    builder.add_node(
    "research_agent",
    research_agent,
    retry=RetryPolicy(
        max_attempts=3,
        retry_on=(Exception,)
    )
    )
    # ==================================================
    # DECISION ROUTING
    # ==================================================

    builder.add_node(
        "recommendation",
        recommendation
    )

    builder.add_node(
        "advance",
        advance
    )

    builder.add_node(
        "reject",
        reject
    )

    builder.add_node(
        "borderline",
        borderline
    )

    # ==================================================
    # HUMAN REVIEW
    # ==================================================

    builder.add_node(
        "human_review",
        human_review
    )

    # ==================================================
    # EMAIL FLOW
    # ==================================================

    builder.add_node(
        "draft_email",
        draft_email
    )

    builder.add_node(
        "critic_loop",
        critic_loop
    )

    builder.add_node(
        "send_email_and_update_ats",
        send_email_and_update_ats,
        retry=RetryPolicy(
            max_attempts=3,
            retry_on=(Exception,)
        )
    )

    # ==================================================
    # REJECTION FLOW
    # ==================================================

    builder.add_node(
        "draft_rejection",
        draft_rejection
    )

    builder.add_node(
        "log_rejection",
        log_rejection
    )

    # ==================================================
    # SAGA
    # ==================================================

    builder.add_node(
        "compensate",
        compensate
    )

    builder.add_node(
        "finalize",
        finalize
    )

    builder.add_node(
        "saver",
        saver
    )

    # retry nodes
    builder.add_node(
    "parser_node",
    parser_node
    )

    builder.add_node(
        "repair_node",
        repair_node
    )

    # ==================================================
    # EDGES
    # ==================================================

    builder.add_edge(
        START,
        "ingest_resume_and_jd"
    )

    builder.add_edge(
        "ingest_resume_and_jd",
        "classify_seniority"
    )

    builder.add_edge(
        "classify_seniority",
        "plan_required_skills"
    )
  

 


    # ORCHESTRATOR FANOUT

    builder.add_conditional_edges(
    "plan_required_skills",
    assign_skill_workers
)

    # PARALLEL SCORERS

    builder.add_edge(
        "plan_required_skills",
        "experience_scorer"
    )

    builder.add_edge(
        "plan_required_skills",
        "education_scorer"
    )

    builder.add_edge(
        "plan_required_skills",
        "signal_scorer"
    )

    builder.add_edge(
        "experience_scorer",
        "wait_for_all"
    )

    builder.add_edge(
        "education_scorer",
        "wait_for_all"
    )

    builder.add_edge(
        "signal_scorer",
        "wait_for_all"
    )

    builder.add_edge(
        "skill_worker",
        "wait_for_all"
    )

    # RESEARCH BRANCH

    builder.add_edge(
        "plan_required_skills",
        "research_agent"
    )

  

    # builder.add_conditional_edges(
    #     "research_agent",
    #     tools_condition,
    #     {
    #         "tools": "tool_node",
    #         "__end__": "aggregate_scores"
    #     }
    # )

    builder.add_conditional_edges(
    "research_agent",
    tools_condition,
    {
        "tools": "tool_node",
        "__end__": "parser_node"
    }
    )

    
    
 
    builder.add_edge(
    "tool_node",
    "research_agent"
    )

    builder.add_edge(
        "aggregate_scores",
        "recommendation"
    )

    

    # error hanfling 
    builder.add_conditional_edges(
    "parser_node",
    parser_router
        )
    
    builder.add_edge(
    "repair_node",
    "research_agent"
)
    

    builder.add_edge(
    "wait_for_all",
    "aggregate_scores"
)

    # ADVANCE FLOW
  
    builder.add_edge(
        "advance",
        "draft_email"
    )

    # BORDERLINE FLOW

    builder.add_edge(
        "borderline",
        "human_review"
    )

    builder.add_conditional_edges(
        "human_review",
        rejection_check,
        {
            "draft_email": "draft_email",
            "draft_rejection": "draft_rejection"
        }
    )

    # ==================================================
    # EMAIL FLOW
    # ==================================================

    builder.add_edge(
        "draft_email",
        "critic_loop"
    )

    builder.add_edge(
        "critic_loop",
        "send_email_and_update_ats"
    )

    # ==================================================
    # REJECTION FLOW
    # ==================================================

    builder.add_edge(
        "reject",
        "draft_rejection"
    )

    builder.add_edge(
        "draft_rejection",
        "log_rejection"
    )

    builder.add_edge(
        "log_rejection",
        "compensate"
    )

    # ==================================================
    # SAGA ROUTING
    # ==================================================


    builder.add_conditional_edges(
    "send_email_and_update_ats",
    ats_result_router
)
    
    builder.add_edge(
        "compensate",
        "finalize"
    )

  

    builder.add_edge("finalize", "saver")
    builder.add_edge("saver", END)
    

    return builder.compile(
        checkpointer=MemorySaver()
    )



# graph = build_graph()
# print(graph)