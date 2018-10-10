# specify the node base image with your desired version node:<version>
FROM node:10-stretch
# replace this with your application's default port
WORKDIR /home/node/app
#ADD ./crouton/* .
#ADD ./crouton/* .
#RUN chown -R node:node .
#RUN npm install 
#RUN npm audit fix 
RUN npm install -g grunt-cli 
RUN npm install grunt --save-dev
#USER node

EXPOSE 9000

#CMD ['tail', '-f', '/dev/null']
CMD ['grunt']
