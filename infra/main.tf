####################################################
# Module: APIs
####################################################
module "apis" {
  source     = "./modules/apis"
  project_id = var.project_id
}


####################################################
# Module: GCS Backups
####################################################
module "gcs_backups" {
  source      = "./modules/gcs"
  bucket_name = "${var.project_id}-db-backups"
  location    = var.region
}


####################################################
# Module: Cloud SQL
####################################################
module "cloudsql" {
  source = "./modules/cloudsql"

  instance_name = "billing-postgres"
  region        = var.region

  database_name = "billing"
  db_user       = "billing_user"
  db_password   = var.db_password
}