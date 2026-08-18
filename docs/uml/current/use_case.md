# Use case — current

Actors: learner, instructor, curriculum maintainer, prospective supervisor. WAIKE does not grant degrees or carrier certificates.

```mermaid
flowchart LR
  subgraph actors
    L[Learner]
    I[Instructor]
    M[Maintainer]
    S[Prospective supervisor]
  end
  subgraph waike [waike-research-ops]
    UC1[Open a digital-RC start packet]
    UC2[Complete a runnable lab JSON]
    UC3[Follow a rubric without keys]
    UC4[Track anonymous artifact completion]
    UC5[Facilitate with instructor packet]
    UC6[Validate schema and provenance]
  end
  L --> UC1
  L --> UC2
  L --> UC3
  L --> UC4
  I --> UC5
  I --> UC3
  M --> UC6
  S --> UC6
  S --> UC1
```

Counts: **14** `curriculum/digital_rc/*/course.json` packages (do not claim 18 for COURSE_DIGITAL_RC). Catalog YAML lists **18** course_ids as a separate universe.
