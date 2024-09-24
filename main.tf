provider "aws" {
  region = "your-region"
}

resource "aws_instance" "django_server" {
  ami           = "ami-123456" # Use a valid AMI
  instance_type = "t2.micro"
  key_name      = "your-key-pair"

  user_data = <<-EOF
              #!/bin/bash
              docker pull <aws_account_id>.dkr.ecr.<region>.amazonaws.com/your-repository:latest
              docker stop django_container || true
              docker rm django_container || true
              docker run -d --name django_container -p 8000:8000 <aws_account_id>.dkr.ecr.<region>.amazonaws.com/your-repository:latest
              EOF

  tags = {
    Name = "DjangoServer"
  }
}
