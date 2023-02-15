resource "digitalocean_droplet" "fast-api" {
  image = "docker-20-04"
  name = "fast-api"
  region = "nyc3"
  size = "s-1vcpu-1gb"
  ssh_keys = [
    data.digitalocean_ssh_key.terraform.id
  ]
  
  connection {
    host = self.ipv4_address
    user = "root"
    type = "ssh"
    private_key = file(var.pvt_key)
    timeout = "2m"
  }
  
# I think docker-compose should already be present on the droplet
# but it was not being found

  provisioner "remote-exec" {
    inline = [
      "export PATH=$PATH:/usr/bin",
      "sudo apt update",
      "curl -L 'https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)' -o /usr/local/bin/docker-compose",
      "chmod +x /usr/local/bin/docker-compose".
      "cd ~/root",
      "git clone https://github.com/coyotespike/fast-api-ocean.git",
      "cd ~/fast-api-ocean",
      "docker-compose up -d --build"
    ]
  }
}