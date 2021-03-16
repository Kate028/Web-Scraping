# Web-Scraper
Required libraries

 >pip install beautifulsoup4

 >pip install lxml 
 
 >pip install requests

## What Is Web Scraping?

Web scraping is the process of gathering information from the Internet.
Most of this data is unstructured data in an HTML format which is then converted into structured data in a spreadsheet or a database so that it can be used in various applications. 

There are many different ways to perform web scraping to obtain data from websites. these include using online services, particular API’s or even creating your code for web scraping from scratch. 

Many large websites like Google, Twitter, Facebook, StackOverflow, etc. have API’s that allow you to access their data in a structured format. 

This is the best option but there are other sites that don’t allow users to access large amounts of data in a structured form or they are simply not that technologically advanced. In that situation, it’s best to use Web Scraping to scrape the website for data.

## Why Scrape the Web?

Automated web scraping can be a solution to speed up the data collection process. You write your code once and it will get the information you want many times and from many pages.

## Challenges of Web Scraping

The Web has grown organically out of many sources. It combines a ton of different technologies, styles, and personalities, and it continues to grow to this day. In other words, the Web is kind of a hot mess! This can lead to a few challenges you’ll see when you try web scraping.

One challenge is variety. Every website is different. While you’ll encounter general structures that tend to repeat themselves, each website is unique and will need its own personal treatment if you want to extract the information that’s relevant to you.

Another challenge is durability. Websites constantly change. 

This is a realistic scenario, as many websites are in active development. Once the site’s structure has changed, your scraper might not be able to navigate the sitemap correctly or find the relevant information. The good news is that many changes to websites are small and incremental, so you’ll likely be able to update your scraper with only minimal adjustments.

However, keep in mind that because the internet is dynamic, the scrapers you’ll build will probably require constant maintenance. You can set up continuous integration to run scraping tests periodically to ensure that your main script doesn’t break without your knowledge.

## APIs: An Alternative to Web Scraping

Some website providers offer Application Programming Interfaces (APIs) that allow you to access their data in a predefined manner. With APIs, you can avoid parsing HTML and instead access the data directly using formats like JSON and XML. HTML is primarily a way to visually present content to users.

When you use an API, the process is generally more stable than gathering the data through web scraping. That’s because APIs are made to be consumed by programs, rather than by human eyes. If the design of a website changes, then it doesn’t mean that the structure of the API has changed.

However, APIs can change as well. Both the challenges of variety and durability apply to APIs just as they do to websites. Additionally, it’s much harder to inspect the structure of an API by yourself if the provided documentation is lacking in quality.

The approach and tools you need to gather information using APIs are outside the scope of this tutorial. To learn more about it, check out API Integration in Python.

## Difference between Web Scraping and API

The goal of both web scraping and APIs is to access web data.
Web scraping allows you to extract data from any website through the use of web scraping software. APIs give you direct access to the data you’d want.

## A few scraping rules

Now that we have the packages we need, we can start scraping. But first, a couple of rules.

 >You should check a site's terms and conditions before you scrape them. It's their data and they likely have some rules to govern it.

 >Be nice - Make the crawling slower, do not slam the server, treat websites nicely. A computer will send web requests much quicker than a user can. 
          Make sure you space out your requests a bit so that you don't hammer the site's server.

 >Scrapers break - Sites change their layout all the time. If that happens, be prepared to rewrite your code.

 >Web pages are inconsistent - There's sometimes some manual clean up that has to happen even after you've gotten your data.

## Scraper tools and bots
Web scraping tools are software (i.e., bots) programmed to sift through databases and extract information. A variety of bot types are used, many being fully customizable to:

 >Recognize unique HTML site structures
 
 >Extract and transform content
 
 >Store scraped data
 
 >Extract data from APIs

## Conclusion

As a result, you might find yourself in a scenario where there might not be an API to access the data you want, or the access to the API might be too limited or expensive.

In these scenarios, web scraping would allow you to access the data as long as it is available on a website.
