Aim to share security practices & latest kinds of attacks, injection style attacks - how to prevent them

Open Web App Security Program - charity dedicated to developing apps with security in mind

XXS - Cross-Site scripting is a very popular injection attack

Injection styled attacks are when we have a form on our website & user fills out form, clicks submit - send data to backend DB

- Rather than entering creds, hackers will enter actual javascript, executable code, so when it gets sent to the backend, the code injected, ran on the backend server
- Example - hacker adds some code to a comment section, now everyon that loads webpage/comments will have that code execute, allowing ability to still user tokens, etc.
- Use owasp prevention guides like using escape chars

SQL Injections - one the most common, oldest kinds of attacks

- Example - blog website with comments, hacker puts JS code in comments, clicks submit, SQL query is sent to backend DB - DELETE all

XSRF - Cross site forgery - injection based

- XSS - delete, modify data
- SQL - delete, modify data
- XSRF - forging a request as if we are someone else, making a admin request.