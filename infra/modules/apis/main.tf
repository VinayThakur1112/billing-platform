resource "google_project_service" "required" {
  for_each = toset([
    "cloudresourcemanager.googleapis.com",
    "iam.googleapis.com",
    "sqladmin.googleapis.com",
    "storage.googleapis.com",
    "serviceusage.googleapis.com"
  ])

  project = var.project_id
  service = each.key

  disable_on_destroy = false
}