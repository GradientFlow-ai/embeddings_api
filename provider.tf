terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

# This environmental variable is defined in .zshrc
# We will pass this variable in via the command line
variable "do_token" {}

# We will pass this variable in via the command line
variable "pvt_key" {}

provider "digitalocean" {
  token = var.do_token
}

# Supposed to add my DO ssh key to any droplets creaetd
# Look under Settings/Security and take the name from there
data "digitalocean_ssh_key" "terraform" {
     name = "terraform" 
}