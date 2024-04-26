Continuous Integration - automating the combination of code from multiple contributors into a single codebase.

1. Source code control
2. Build automation - packaging software
3. Unit testing - automate testing components of software - test-driven development
4. Branch merging
5. Integration testing - testing how components interact with each other

CD - Continuous delivery/deployment - automating the delivery of IT services to users

1. Central repository
2. System testing - testing full app
3. Deployment - automatically accessible to users
4. User-acceptance testing

Integrating, Building, and Testing

- commits usually kickoff pipelines, so you need good SCM
- Maintain a single source repository
- Automate the build process - packaging o r compiling code should be automated
- Use python unittest library for unit testing

Delivery & Deployment

- All about putting the software into the users' hands.
- Ensure code is stored in a centralized backed up location
- Automate system testing to test system (overall) deployment - everything is doing its job
- Manage drifts between master & test branches
- Infra as Code - build system env everytime it runs / immutable infra

Data Security

Data in Transit vs Rest

Transit - when our HQ paries with 3rd party for analytics.. When we transmit the data, we need to make sure the data we send to 3rd part is secure as possible - https, sftp, ssh

Rest - data that is stored somewhere - all storage disks/databases/processes needs to be encrypted

- Using env vars to store script creds

Using wireshark to investigate network traffic over encrypted protocols vs non encrypted

You could be send data in clear-text (telnet) send creds in packet in plain text

Pay for SSL certs for encryption

SSL certificates are what enable websites to use HTTPS, which is more secure than HTTP. An SSL certificate is a data file hosted in a website's origin server. SSL certificates make SSL/TLS encryption possible, and they contain the website's public key and the website's identity, along with related information.

Use environment variables to store creds in OS environment

disk encryption

Use bitlocker for windows / file vault for macOS with appleID / Tomb for linux

SQLServer comes with DB encryption - master key / slave key

Azure cloud DQL DBs use key vault to turn on Always on encryption