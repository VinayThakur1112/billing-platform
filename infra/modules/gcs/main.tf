resource "google_storage_bucket" "backup_bucket" {
  name     = var.bucket_name
  location = var.location

  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle {
    prevent_destroy = true
  }
}