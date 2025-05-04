
---

## ✅ GENERAL GIT WORKFLOW

> All members follow this **branching and commit workflow**:

### 🔁 Workflow

1. Clone the project:

   ```bash
   git clone <your-repo-url>
   ```

2. Create a new branch for your feature:

   ```bash
   git checkout -b feat/<short-description>
   ```

3. Work on the feature.

4. Stage, commit, and push:

   ```bash
   git add .
   git commit -m "feat: add trip assignment API"
   git push origin feat/<short-description>
   ```

5. Open a Pull Request (PR) on GitHub.

6. Get 1 peer review before merging.

---

## 👤 Member 1 — Backend (Authentication & Roles)

**Branch Prefix:** `feat/auth`

### Tasks:

* [ ] Create `User` model with `role` field (admin/manager/driver)
* [ ] Setup JWT-based login and register endpoints
* [ ] Setup role-based permissions
* [ ] Protect views based on roles
* [ ] Add `whoami/` endpoint to get current user info
* [ ] Implement company-based user isolation (multi-tenancy)

**Commit Examples:**

```bash
git commit -m "feat: implement custom user model with role field"
git commit -m "feat: add JWT login and registration"
```

---

## 👤 Member 2 — Backend (Fleet, Trips, Real-time)

**Branch Prefix:** `feat/trips`

### Tasks:

* [ ] Create models for `Vehicle`, `Trip`, `Checkpoint`, `DeliveryProof`
* [ ] Build APIs: list vehicles, create trip, assign driver
* [ ] Add endpoints for trip status updates (accepted, picked up, delivered)
* [ ] Add endpoint for uploading delivery proof (file upload)
* [ ] Setup WebSocket (Django Channels) to notify manager of status updates
* [ ] Add analytics/stats aggregation

**Commit Examples:**

```bash
git commit -m "feat: create Trip model and status flow"
git commit -m "feat: implement WebSocket for trip status updates"
```

---

## 🧑‍💻 Member 3 — Frontend (Admin UI, Auth, Layout)

**Branch Prefix:** `ui/admin`

### Tasks:

* [ ] Set up Vue project + Tailwind or CSS modules
* [ ] Create `LoginView` and `RegisterView` with API connection
* [ ] Store JWT in `localStorage`
* [ ] Create Admin layout (`/admin/*`) with sidebar/navigation
* [ ] Pages: Dashboard, User Management, Fleet Vehicles
* [ ] Implement logout and route protection

**Commit Examples:**

```bash
git commit -m "ui: implement login page and JWT handling"
git commit -m "ui: create admin layout and dashboard"
```

---

## 🧑‍💻 Member 4 — Frontend (Manager & Driver UI)

**Branch Prefix:** `ui/manager-driver`

### Tasks:

* [ ] Create `/manager/dashboard`, `/manager/trips`, `/assign`
* [ ] Trip planner form (origin, destination)
* [ ] Trip assignment UI (dropdown: select driver)
* [ ] `/driver/trips` page (list view)
* [ ] `/driver/trips/:id` (accept/start/update trip)
* [ ] File upload (proof of delivery)
* [ ] Real-time map with trip status (optional with WebSocket)

**Commit Examples:**

```bash
git commit -m "ui: add trip planner and assignment UI for manager"
git commit -m "ui: implement trip lifecycle view for drivers"
```

---

## 📌 Shared Tasks / Optional Enhancements

| Task                                        | Who                |
| ------------------------------------------- | ------------------ |
| Set up Docker & docker-compose for DB/Redis | Any backend member |
| Write API docs in Postman or Swagger        | Backend 1 & 2      |
| UI testing or responsive design             | Frontend 3 & 4     |
| Add loading states and toasts               | Frontend 4         |
| Deploy to Heroku/Render                     | Final week         |

---

Would you like me to generate a shared Trello/Notion task board template or auto-create GitHub issues based on these?
