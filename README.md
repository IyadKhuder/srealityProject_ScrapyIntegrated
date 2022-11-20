# srealityProject_ScrapyIntegrated
This project is based on the previous one: https://github.com/IyadKhuder/srealityProject
However, here I've tried to integrate the Scrapy container in it.
That is, this docker-compose contains the following containers:
1. Scrapy [name: scrapeit] : Integrated and put in service.
2. Database container [name: aptsdb11]: It uses Postgresql.
3. Server container [name: apts]: This uses Node.js.
4. The front-end container: This is a PHP-enriched HTML file.

Althogh all the containers work properly, but there's a problem with the orchestration of the starting order:
The 2nd container (the Postgresql database) takes as input the scraped data, which is the output of the `st one (Scrapy). 
The scraped data are exported as a CSV file (in this project named: result.csv). 
Thus, the 2nd container cannot (and should not) work before result.csv has been created.
Although docker-compose provides the keyword "depends on", to tell which conatiner is a dependency of a certain container, 
but this unfortunately only orchesters the starting time of the containers, 
which means, the 2nd container does not start before the 1st one is running,
but this still allows the 2nd one to start before the 1st one achieves its tasks! And here comes the problem.

Having searched for a solution to this problem, I've tried two methods:
a. I've come up with a tool named: wait-for, 
which is suggested in the official docker documentation: https://docs.docker.com/compose/startup-order/
b. The use of "healthcheck" test in the 1st container and the "service_healthy" condition in the latter one.
However, I haven't been able to make use out of either of the two methods, so far.



