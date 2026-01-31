output "db_host" {
  value = google_sql_database_instance.postgres.public_ip_address
}

output "db_name" {
  value = google_sql_database.app_db.name
}

output "db_user" {
  value = google_sql_user.app_user.name
}