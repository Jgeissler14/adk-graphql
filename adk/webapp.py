"""Flask web interface for interacting with the team lead agent."""

from __future__ import annotations

from flask import Flask, render_template, request, redirect, url_for

from .hospital_consultant import run_team_lead, context_store

app = Flask(__name__)

# Available team leads could be extended in the future
TEAM_LEADS = {
    "hospital": {
        "name": "Hospital Consultant Team Lead",
        "runner": run_team_lead,
    }
}

COMPANY_ID = "demo_company"
USER_ID = "demo_user"


@app.route("/")
def select_team_lead():
    """Homepage for selecting which team lead to chat with."""
    return render_template("select_lead.html", team_leads=TEAM_LEADS)


@app.route("/chat/<lead>", methods=["GET", "POST"])
def chat(lead: str):
    """Chat page for the given team lead."""
    if lead not in TEAM_LEADS:
        return "Unknown team lead", 404

    if request.method == "POST":
        message = request.form.get("message", "")
        if message:
            TEAM_LEADS[lead]["runner"](COMPANY_ID, USER_ID, message)
        return redirect(url_for("chat", lead=lead))

    history = context_store.get_user_history(COMPANY_ID, USER_ID)
    return render_template(
        "chat.html", lead=TEAM_LEADS[lead]["name"], history=history
    )
