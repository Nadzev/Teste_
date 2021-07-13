FROM debian:latest
LABEL description='imagem de teste' maintainer="Nádila <ndsda.eng19@uea.edu.br"
RUN apt-get update && apt-get upgrade -y
RUN apt-get install nginx -y

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]