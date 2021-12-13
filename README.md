 # Hackaton 2021

 ## Before starting
 See `Deployment` and `Pre-requisites` to know how to install and deploy the project

 ## Pre-requisites
 * Docker
 * Docker-compose

 ## Make commands
 ```
 make up
 -- Start the containers
 ```

 ```
 make stop
 -- Stop docker containers whitout removing them
 ```

 ```
 make down
 -- Stop and remove docker containers
 ```

 ```
 make build
 -- Rebuild docker image
 ```
 ## Dev commands
 This commands only work's inside backend container, for use it, you must use `make up` first
 ```
 dev up
 -- Run the application
 ```

 ```
 dev pipi
 -- Install requirements
 ```

 ```
 dev makemig
 -- Make migrations
 ```

 ```
 dev migrate
 -- Migrate pending migrations
 ```

 ```
 dev test
 -- Run tests
 ```

 ```
 dev createapp <APP_NAME>
 -- Create Django App
 ```

 ## Before making a pull request
 1. Run tests `dev test`
 2. Run black `black .` if is necesary
 3. Test your code on local
 4. Make atomic commits with karma format http://karma-runner.github.io/6.0/dev/git-commit-msg.html
 5. Work on a diferent brach for each pull request, the name of this brach must be accord with this format
 ```
 feat: For new features
 ```
 ```
 chore: For modifications on existing code
 ```
 ```
 fix: For fixes and bug resolves
 ```

 ## Development process on local
 1. Start the containers with `make up`
 2. Inside the backend container install the depencencies with `dev pipi`
 3. Run the application with `dev up`
 4. Code


 ## Hackaton 2021