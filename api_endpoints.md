# 📡 SkillLink API Endpoints

## 🔐 Auth
- `POST /register` – Register as player or org
- `POST /login` – Login and receive token
- `GET /me` – Get logged-in user profile (Auth)
- `PATCH /me` – Update user profile (Auth)

---

## 🎯 Gigs
- `POST /gigs` – Post a new gig (Org, Auth)
- `GET /gigs` – List all gigs
- `GET /gigs/{gig_id}` – Get single gig
- `GET /my_gigs` – View gigs posted by org (Auth)

---

## 📥 Applications
- `POST /apply` – Apply to a gig (Player, Auth)
- `GET /applications/{gig_id}` – View applicants for a gig (Org, Auth)
- `GET /my_applications` – View all gigs a player applied to (Player, Auth)

---

## 💬 Endorsements
- `POST /endorse` – Endorse a player (Org, Auth)
- `GET /endorsements/{user_id}` – View endorsements of a user
- `DELETE /endorsements/{endorsement_id}` – Delete endorsement (Org, Auth)

---

## 🧪 Stat Verification
- `POST /connect-stats` – Save external ID (Player, Auth)
- `POST /verify-stats` – Verify stats (Player, Auth)

---

## 🏆 Soulbound NFT
- `POST /mint_soulbound_nft?user_id=...` – Mint NFT (Backend checks eligibility)
- `GET /nft/{user_id}` – View NFT by user ID

---

## ⚙️ Admin
- `GET /admin/stats` – Platform stats (Admin only)

