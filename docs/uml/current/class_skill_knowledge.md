# Class — skill / knowledge (current)

File-backed types, not a learned knowledge graph.

```mermaid
classDiagram
  class CatalogCourse {
    course_id
    course_title
    program_track
    level
  }
  class DigitalRcPackage {
    schema waike.course_package.v1
    weeks
    labs
    assessments
    rubrics
    provenance
  }
  class Pathway {
    start
    prereqs
    objectives
    lessons
    labs
    completion_tracking
    instructor_guidance
  }
  class SkillDomain {
    id
    beginner_outcomes
    intermediate_outcomes
    advanced_outcomes
    repo_links
  }
  class CompletionRecord {
    course_id
    week
    artifact_id
    artifact_submitted
    opaque_learner_ref
    pii_forbidden
  }
  CatalogCourse --> DigitalRcPackage : mapped when RC exists
  DigitalRcPackage --> Pathway : overlay
  SkillDomain --> CatalogCourse : knowledge_maps
  Pathway --> CompletionRecord
```

Sources: `curriculum/catalog.yaml`, `schema/waike_course_package.v1.json`, `schema/waike_pathway.v1.json`, `knowledge_maps/waike_skill_tree.yaml`, `schema/waike_completion_tracking.v1.json`.
