from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[2]
CAMPUSES = ["gary", "ghana", "guyana", "gaza", "geelong", "graham_land", "germany"]

FLAGSHIP_CASE_STUDIES: dict[str, list[dict[str, str]]] = {
    "gary": [
        {"case_id": "homework_portfolio_access_lab", "title": "Homework and Portfolio Access Lab"},
        {"case_id": "family_digital_navigation_night", "title": "Family Digital Navigation Night"},
        {"case_id": "small_business_digital_starter_kit", "title": "Small Business Digital Starter Kit"},
        {"case_id": "public_wifi_quality_map", "title": "Public Wi-Fi Quality Map"},
        {"case_id": "outage_learning_cache", "title": "Outage Learning Cache"},
    ],
    "ghana": [
        {"case_id": "solar_powered_learning_hub", "title": "Solar-Powered Learning Hub"},
        {"case_id": "mobile_first_workforce_training", "title": "Mobile-First Workforce Training"},
        {"case_id": "agriculture_market_information_lab", "title": "Agriculture and Market Information Lab"},
        {"case_id": "mobile_money_cybersecurity_workshop", "title": "Mobile Money Cybersecurity Workshop"},
        {"case_id": "power_backhaul_failure_drill", "title": "Power and Backhaul Failure Drill"},
    ],
    "guyana": [
        {"case_id": "hinterland_ict_hub_support", "title": "Hinterland ICT Hub Support"},
        {"case_id": "e_government_assistance_desk", "title": "E-Government Assistance Desk"},
        {"case_id": "local_technician_apprenticeship", "title": "Local Technician Apprenticeship"},
        {"case_id": "flood_resilience_connectivity_plan", "title": "Flood Resilience Connectivity Plan"},
        {"case_id": "offline_telehealth_support", "title": "Offline Telehealth Support"},
    ],
    "gaza": [
        {"case_id": "remote_first_education_continuity_kit", "title": "Remote-First Education Continuity Kit"},
        {"case_id": "crisis_learning_archive", "title": "Crisis Learning Archive"},
        {"case_id": "reconstruction_skills_pathway", "title": "Reconstruction Skills Pathway"},
        {"case_id": "blackout_resilient_content_plan", "title": "Blackout-Resilient Content Plan"},
        {"case_id": "safe_data_no_tracking_mode", "title": "Safe Data / No-Tracking Mode"},
    ],
    "geelong": [
        {"case_id": "inclusive_smart_city_lab", "title": "Inclusive Smart-City Lab"},
        {"case_id": "disability_first_device_os_testing", "title": "Disability-First Device and OS Testing"},
        {"case_id": "youth_creative_tech_studio", "title": "Youth Creative-Tech Studio"},
        {"case_id": "emergency_digital_services", "title": "Emergency Digital Services"},
        {"case_id": "mobile_only_affordability_mapping", "title": "Mobile-Only Affordability Mapping"},
    ],
    "graham_land": [
        {"case_id": "polar_ntn_simulation", "title": "Polar NTN Simulation"},
        {"case_id": "offline_scientific_workflow", "title": "Offline Scientific Workflow"},
        {"case_id": "priority_aware_data_sync", "title": "Priority-Aware Data Sync"},
        {"case_id": "satellite_outage_mode", "title": "Satellite Outage Mode"},
        {"case_id": "low_power_emergency_mode", "title": "Low-Power Emergency Mode"},
    ],
    "germany": [
        {"case_id": "privacy_security_equity_lab", "title": "Privacy/Security Equity Lab"},
        {"case_id": "industry_4_apprenticeship_bridge", "title": "Industry 4.0 Apprenticeship Bridge"},
        {"case_id": "older_adult_digital_confidence", "title": "Older Adult Digital Confidence"},
        {"case_id": "rural_outage_fallback", "title": "Rural Outage Fallback"},
        {"case_id": "multilingual_service_navigation", "title": "Multilingual Service Navigation"},
    ],
}


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    if yaml:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    import json
    return json.loads(path.read_text(encoding="utf-8"))


def load_catalog() -> dict[str, Any]:
    return _load_yaml(ROOT / "curriculum" / "catalog.yaml")


def load_assessment_model() -> dict[str, Any]:
    return _load_yaml(ROOT / "curriculum" / "assessment_model.yaml")


def courses() -> list[dict[str, Any]]:
    return load_catalog().get("courses", [])


COURSES = courses
