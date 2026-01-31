variable "instance_name" {
  type = string
}

variable "region" {
  type = string
}

variable "tier" {
  type    = string
  default = "db-f1-micro"
}

variable "database_name" {
  type = string
}

variable "db_user" {
  type = string
}

variable "db_password" {
  type      = string
  sensitive = true
}