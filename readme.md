┌─────────────────────────────────────────────────────────────────────────────┐
│                         SCHOOL MANAGEMENT SYSTEM                            │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────┐        ┌─────────────────┐        ┌──────────────┐
│    SCHOOL    │        │  ACADEMIC_YEAR  │        │  DEPARTMENT  │
│──────────────│1      N│─────────────────│        │──────────────│
│ id (PK)      │───────▶│ id (PK)         │        │ id (PK)      │
│ name         │        │ school_id (FK)  │        │ school_id(FK)│
│ address      │        │ name            │        │ name         │
│ phone        │1      N│ start_date      │        │ code         │
│ email        │───────▶│ end_date        │        └──────┬───────┘
│ established  │        │ is_active       │               │1
└──────┬───────┘        └────────┬────────┘               │
       │1                        │1                        │
       │                    ┌────┴────┐              ┌─────┴──────┐
       │N                   │N        │N             │N           │N
       ▼                    ▼         ▼              ▼            ▼
┌────────────┐        ┌──────────┐ ┌──────┐  ┌──────────┐ ┌─────────┐
│   NOTICE   │        │  CLASS   │ │ EXAM │  │ SUBJECT  │ │ TEACHER │
│────────────│        │──────────│ │──────│  │──────────│ │─────────│
│ id (PK)    │        │ id (PK)  │ │id(PK)│  │ id (PK)  │ │ id (PK) │
│school_id FK│        │dept_id FK│ │yr_id │  │ dept_id  │ │ user_id │
│created_by  │        │yr_id  FK │ │name  │  │ name     │ │ dept_id │
│ title      │        │ name     │ │type  │  │ code     │ │ emp_id  │
│ content    │        │ section  │ │start │  │ credits  │ │ qual.   │
│ audience   │        │ capacity │ │end   │  │ type     │ │join_date│
└────────────┘        └────┬─────┘ └──┬───┘  └────┬─────┘ └────┬────┘
                           │1         │1           │1           │1
                      ┌────┴────┐     │            │            │
                      │N        │N    │N           │N           │N
                      ▼         ▼     ▼            ▼            └──────────┐
                ┌─────────┐ ┌──────────────────────────────────┐           │
                │ STUDENT │ │           CLASS_SUBJECT           │           │
                │─────────│ │──────────────────────────────────│◀──────────┘
                │ id (PK) │ │ id (PK)                          │
                │user_id  │ │ class_id   (FK) ─────────────────┘ (from CLASS)
                │class_id │ │ subject_id (FK) ─────────────────  (from SUBJECT)
                │roll_no  │ │ teacher_id (FK) ─────────────────  (from TEACHER)
                │adm_no   │ └──────────┬───────────────────────┘
                │dob      │            │1
                │gender   │      ┌─────┼──────────┐
                └────┬────┘      │1    │1          │1
                     │           │N    │N          │N
                     │           ▼     ▼           ▼
                     │    ┌──────────┐ ┌─────────┐ ┌───────────────┐
                     │    │TIMETABLE │ │ATTEND.  │ │ EXAM_SCHEDULE │
                     │    │──────────│ │─────────│ │───────────────│
                     │    │ id (PK)  │ │ id (PK) │ │ id (PK)       │
                     │    │cs_id  FK │ │cs_id FK │ │ exam_id    FK │
                     │    │day       │ │stud_id  │ │ cs_id      FK │
                     │    │start_time│ │date     │ │ exam_datetime │
                     │    │end_time  │ │status   │ │ duration_mins │
                     │    │room      │ │remarks  │ │ max_marks     │
                     │    └──────────┘ └────▲────┘ │ pass_marks    │
                     │                      │       └──────┬────────┘
                     └──────────────────────┘N             │1
                     │1                                     │N
                     │                                      ▼
                     │N                             ┌──────────────┐
                     ▼                              │    RESULT    │
              ┌─────────────┐                       │──────────────│
              │ FEE_PAYMENT │                       │ id (PK)      │
              │─────────────│                       │ schedule_id  │
              │ id (PK)     │                       │ student_id   │
              │ student_id  │                       │ marks        │
              │ fee_str_id  │                       │ grade        │
              │ amount_paid │                       │ is_absent    │
              │ pay_date    │                       └──────────────┘
              │ method      │
              │ status      │
              │ receipt_no  │
              └──────▲──────┘
                     │N
                     │
              ┌──────┴──────────┐
              │  FEE_STRUCTURE  │
              │─────────────────│
              │ id (PK)         │
              │ academic_yr_id  │
              │ class_id        │
              │ fee_type        │
              │ amount          │
              │ due_date        │
              │ is_optional     │
              └─────────────────┘


  USER AUTH LAYER
  ───────────────────────────────────────────────
  ┌──────────────┐
  │     USER     │
  │──────────────│
  │ id (PK)      │
  │ email        │  1:1        ┌──────────┐
  │ username     │────────────▶│ TEACHER  │
  │ password     │             └──────────┘
  │ role         │  1:1        ┌──────────┐
  │ phone        │────────────▶│ STUDENT  │
  │ is_active    │             └──────────┘
  └──────────────┘  1:1         ┌──────────┐
                   ────────────▶│  PARENT  │
                                └──────────┘

  STUDENT ◀────────────── STUDENT_PARENT ──────────────▶ PARENT
  (1)          N:M junction table         (1)
               ┌─────────────────┐
               │ STUDENT_PARENT  │
               │─────────────────│
               │ id (PK)         │
               │ student_id (FK) │
               │ parent_id  (FK) │
               │ is_primary      │
               └─────────────────┘


  RELATIONSHIP LEGEND
  ───────────────────
  1 ──────▶ N    One to Many
  1 ──────▶ 1    One to One  (1:1)
  N ◀──── N      Many to Many (via junction table)
  (FK)           Foreign Key
  (PK)           Primary Key
  