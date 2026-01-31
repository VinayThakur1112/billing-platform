resource "google_sql_database_instance" "postgres" {
  name             = var.instance_name
  database_version = "POSTGRES_14"
  region           = var.region

  deletion_protection = false

  settings {
    tier = var.tier

    availability_type = "ZONAL"

    backup_configuration {
      enabled = false
    }

    ip_configuration {
      ipv4_enabled = true
    }
  }
}

resource "google_sql_database" "app_db" {
  name     = var.database_name
  instance = google_sql_database_instance.postgres.name
}

resource "google_sql_user" "app_user" {
  name     = var.db_user
  password = var.db_password
  instance = google_sql_database_instance.postgres.name
}