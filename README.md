# ChromaDB API

This microservice will serve as the embeddings database.


## Terraform Usage

This simple task creates a digital ocean droplet, then clones a git repo and runs docker-compose to build and run a FastAPI service.

terraform plan \
  -var "do_token=${DO_PAT}" \
  -var "pvt_key=$HOME/.ssh/id_rsa"


terraform apply \
  -var "do_token=${DO_PAT}" \
  -var "pvt_key=$HOME/.ssh/id_rsa"

terraform state list

terraform destroy \
  -var "do_token=${DO_PAT}" \
  -var "pvt_key=$HOME/.ssh/id_rsa"


May need sometime: https://registry.terraform.io/providers/integrations/github/latest/docs/resources/repository_deploy_key

## Installing again

Recreating the resource is a good test of this pipeline, but a real CI/CD pipeline is needed.

- Add the deploy key automatically
