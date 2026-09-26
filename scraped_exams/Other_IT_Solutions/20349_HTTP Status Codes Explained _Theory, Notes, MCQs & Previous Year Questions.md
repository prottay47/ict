# HTTP Status Codes Explained |Theory, Notes, MCQs & Previous Year Questions

- **Original URL:** [https://it.jobqns.com/http-status-codes-explained-theory-notes-mcqs-previous-year-questions/](https://it.jobqns.com/http-status-codes-explained-theory-notes-mcqs-previous-year-questions/)
- **Date:** 2026-07-07T14:24:57
- **Categories:** Uncategorized

---

Topic Wise Question Bank

All Topics

Category: HTTP Status Code

- ☆

1

Theory

HTTP Status Codes – Complete Theory, Categories, Working Process, and Common Status Codes

Web_technology
| HTTP Status Code

**HTTP Status Codes**

Whenever you browse the Internet, your web browser and the web server communicate with each other using  **HTTP (HyperText Transfer Protocol)** . Every time you open a webpage, click a link, submit a form, upload a file, or use an API, your browser sends an  **HTTP Request**  to the server. The server processes that request and sends back an  **HTTP Response** .

Along with the response, the server also sends a  **three-digit HTTP Status Code** . This status code tells the browser what happened to the request. It informs whether the request was successful, whether the requested resource has moved, whether the client made an error, or whether the server encountered a problem while processing the request.

You can think of an  **HTTP Status Code**  as a communication language between the  **Client**  (Browser or Application) and the  **Server** . Without these status codes, the browser would not know whether to display a webpage, redirect the user, ask for authentication, or show an error message.

For web developers, website owners, API developers, and SEO professionals, understanding HTTP Status Codes is very important. They help identify website problems, improve user experience, troubleshoot server issues, optimize website performance, and maintain good search engine rankings.

**Why are HTTP Status Codes Important?**

HTTP Status Codes are important because they provide clear information about the result of every HTTP Request. They help both users and developers understand what happened during the communication between the browser and the server.

They inform whether a request was successful or failed.
They help browsers decide how to handle the server response.
They help developers troubleshoot website and API problems.
They improve website maintenance and debugging.
They play an important role in Search Engine Optimization (SEO).
They help improve website security and performance.
They support browser caching and resource optimization.

**How HTTP Status Codes Work**

The communication between a browser and a web server follows a simple process known as the  **HTTP Request-Response Cycle** .

The user enters a website URL or clicks a hyperlink.
The browser sends an  **HTTP Request**  to the web server.
The server receives and processes the request.
The server generates an  **HTTP Response** .
The response contains the requested resource along with an  **HTTP Status Code** .
The browser reads the status code and decides what action to perform.

For example, if the server returns  **200 OK** , the browser displays the webpage. If it returns  **301 Moved Permanently** , the browser automatically redirects the user to the new URL. If it returns  **404 Not Found** , the browser displays an error page because the requested resource does not exist.

**The Five Categories of HTTP Status Codes**

Every HTTP Status Code belongs to one of five categories. The category is determined by the  **first digit**  of the status code. Even if you have never seen a particular status code before, you can understand its general meaning simply by looking at its first digit.

Category
Description
Examples

**1xx**
Informational Responses
100, 101

**2xx**
Successful Responses
200, 201, 204, 206

**3xx**
Redirection Responses
301, 302, 304, 307, 308

**4xx**
Client Error Responses
400, 401, 403, 404, 405, 408, 429

**5xx**
Server Error Responses
500, 501, 502, 503, 504

Each category represents a different type of response. Understanding these categories makes it easier to diagnose website problems, develop web applications, and prepare for technical interviews and competitive examinations.

**Real-Life Example**

Suppose you visit the website  **https://example.com/login** .

If the login page opens normally, the server returns  **200 OK** .
If the login page has permanently moved to another URL, the server returns  **301 Moved Permanently** , and the browser automatically redirects you.
If you enter a wrong URL such as  **/loginn** , the server may return  **404 Not Found** .
If the login page requires authentication before access, the server may return  **401 Unauthorized** .
If the server crashes while processing your request, it may return  **500 Internal Server Error** .

In every case, the browser uses the HTTP Status Code to determine how the request should be handled and what information should be shown to the user.


**HTTP Status Codes (বাংলা)**

আপনি যখন ইন্টারনেট ব্রাউজ করেন, তখন আপনার  **Web Browser**  এবং  **Web Server**  একে অপরের সাথে  **HTTP (HyperText Transfer Protocol)**  এর মাধ্যমে যোগাযোগ করে। প্রতিবার আপনি কোনো Website খুলেন, Link-এ Click করেন, Form Submit করেন, File Upload করেন অথবা কোনো API ব্যবহার করেন, তখন আপনার Browser একটি  **HTTP Request**  Server-এর কাছে পাঠায়। এরপর Server সেই Request Process করে একটি  **HTTP Response**  Browser-এ ফেরত পাঠায়।

এই  **HTTP Response** -এর সাথে Server একটি  **তিন অঙ্কের (Three-digit) HTTP Status Code**  পাঠায়। এই Status Code Browser-কে জানায় Request-এর ফলাফল কী হয়েছে। অর্থাৎ Request সফল হয়েছে কিনা, Resource অন্য কোথাও স্থানান্তরিত হয়েছে কিনা, Client কোনো ভুল করেছে কিনা, অথবা Server-এর কোনো সমস্যা হয়েছে কিনা—এসব তথ্য Status Code-এর মাধ্যমে জানা যায়।

সহজভাবে বলা যায়,  **HTTP Status Code**  হলো  **Client**  (Browser বা Application) এবং  **Server** -এর মধ্যে যোগাযোগের একটি সাধারণ ভাষা (Communication Language)। Browser এই Code দেখে বুঝতে পারে তাকে Webpage দেখাতে হবে, অন্য URL-এ Redirect করতে হবে, User-এর Authentication চাইতে হবে, নাকি একটি Error Message প্রদর্শন করতে হবে।

Web Developer, Website Owner, API Developer এবং SEO Professional-দের জন্য  **HTTP Status Code**  সম্পর্কে ধারণা থাকা অত্যন্ত গুরুত্বপূর্ণ। কারণ এগুলো Website-এর সমস্যা শনাক্ত করতে, Debugging করতে, Performance উন্নত করতে, User Experience ভালো রাখতে এবং Search Engine Ranking বজায় রাখতে গুরুত্বপূর্ণ ভূমিকা পালন করে।

**HTTP Status Codes কেন গুরুত্বপূর্ণ?**

প্রতিটি  **HTTP Request** -এর ফলাফল কী হয়েছে তা পরিষ্কারভাবে জানাতে  **HTTP Status Code**  ব্যবহার করা হয়। এটি শুধু Browser-কে নয়, Developer-কেও বুঝতে সাহায্য করে Client এবং Server-এর মধ্যে কী ঘটেছে।

Request সফল হয়েছে নাকি ব্যর্থ হয়েছে তা জানা যায়।
Browser বুঝতে পারে পরবর্তী কী কাজ করতে হবে।
Developer সহজে Website এবং API-এর সমস্যা শনাক্ত (Troubleshoot) করতে পারে।
Website-এর Debugging ও Maintenance সহজ হয়।
SEO-এর জন্য গুরুত্বপূর্ণ তথ্য প্রদান করে।
Website-এর Security এবং Performance উন্নত করতে সাহায্য করে।
Browser Caching এবং Resource Optimization-এ সহায়তা করে।

**HTTP Status Codes কীভাবে কাজ করে?**

**Browser**  এবং  **Server** -এর মধ্যে যোগাযোগ একটি নির্দিষ্ট ধাপে সম্পন্ন হয়, যাকে  **HTTP Request–Response Cycle**  বলা হয়।

User একটি Website-এর URL লিখে অথবা কোনো Link-এ Click করে।
Browser একটি  **HTTP Request**  Server-এ পাঠায়।
Server Request গ্রহণ করে এবং Process করে।
Server একটি  **HTTP Response**  তৈরি করে।
Response-এর সাথে একটি  **HTTP Status Code**  পাঠানো হয়।
Browser Status Code পড়ে সিদ্ধান্ত নেয় Webpage দেখাবে, Redirect করবে নাকি Error Page প্রদর্শন করবে।

উদাহরণস্বরূপ, যদি Server  **200 OK**  পাঠায়, তাহলে Browser বুঝতে পারে Request সফল হয়েছে এবং Webpage প্রদর্শন করে। যদি  **301 Moved Permanently**  পাঠায়, তাহলে Browser স্বয়ংক্রিয়ভাবে নতুন URL-এ Redirect করে। আবার  **404 Not Found**  পাঠালে Browser বুঝতে পারে চাওয়া Resource খুঁজে পাওয়া যায়নি এবং একটি Error Page দেখায়।

**HTTP Status Codes-এর পাঁচটি প্রধান Category**

সব  **HTTP Status Code**  পাঁচটি প্রধান Category-এর মধ্যে বিভক্ত। কোনো Status Code-এর  **প্রথম সংখ্যা (First Digit)**  দেখেই বোঝা যায় সেটি কোন Category-এর অন্তর্ভুক্ত এবং সাধারণভাবে তার অর্থ কী।

Category
অর্থ
উদাহরণ

**1xx**
Informational Responses (তথ্য প্রদানকারী Response)
100, 101

**2xx**
Successful Responses (সফল Response)
200, 201, 204, 206

**3xx**
Redirection Responses (Redirect Response)
301, 302, 304, 307, 308

**4xx**
Client Error Responses (Client-এর ভুল)
400, 401, 403, 404, 405, 408, 429

**5xx**
Server Error Responses (Server-এর সমস্যা)
500, 501, 502, 503, 504

এই পাঁচটি Category সম্পর্কে ভালো ধারণা থাকলে Website-এর সমস্যা দ্রুত শনাক্ত করা, Web Application তৈরি করা এবং বিভিন্ন চাকরির পরীক্ষা বা Interview-এর প্রশ্নের উত্তর দেওয়া অনেক সহজ হয়ে যায়।

**বাস্তব উদাহরণ (Real-Life Example)**

ধরুন আপনি  **https://example.com/login**  Website-এ প্রবেশ করতে চান।

যদি Login Page সফলভাবে Open হয়, তাহলে Server  **200 OK**  পাঠায়।
যদি Login Page স্থায়ীভাবে অন্য URL-এ স্থানান্তরিত হয়ে থাকে, তাহলে Server  **301 Moved Permanently**  পাঠায় এবং Browser স্বয়ংক্রিয়ভাবে নতুন URL-এ Redirect করে।
যদি আপনি ভুল URL যেমন  **/loginn**  লিখেন, তাহলে Server  **404 Not Found**  পাঠাতে পারে।
যদি Login করার আগে Authentication প্রয়োজন হয়, তাহলে Server  **401 Unauthorized**  পাঠাতে পারে।
যদি Server-এর অভ্যন্তরীণ (Internal) কোনো সমস্যা হয়, তাহলে Server  **500 Internal Server Error**  পাঠাতে পারে।

অর্থাৎ, প্রতিটি  **HTTP Status Code**  Browser-কে জানিয়ে দেয় Request-এর ফলাফল কী হয়েছে এবং Browser সেই অনুযায়ী User-কে সঠিক তথ্য বা Webpage প্রদর্শন করে।

- ☆

2

Previous Question
Combined Bank, ADA-23, 26

A mobile banking application successfully connects to a server and attempts to upload a customer document, but the server rejects the request because the uploaded file format is not supported. Which HTTP status code should be returned and why?[assume]

Web_technology
| HTTP Status Code

**Correct Status Code: 415 Unsupported Media Type**

The server should return  **415 Unsupported Media Type**  because the uploaded file format violates the server's accepted content types.

**Why 415 is the Right Choice**

**Client error category:**  4xx codes indicate the problem is on the client side. The request was understood but cannot be processed due to invalid content.
**Specific to content type:**  415 explicitly signals that the server refuses to accept the payload because its media type is not supported, unlike generic 400 which covers all bad requests.
**Content-Type header mismatch:**  The client likely sent a Content-Type header (e.g.,
```
image/heic
```
or
```
application/x-bittorrent
```
) that the server does not allow for document uploads.

**Response Example:**

```
HTTP/1.1 415 Unsupported Media Type
Content-Type: application/json
{
"error": "Unsupported file format",
"message": "Only PDF, JPG, and PNG files are accepted",
"received": "image/webp",
"allowed_types": ["application/pdf", "image/jpeg", "image/png"]
}
```

**Why Not Other Codes?**

Code
Why Incorrect

**400 Bad Request**
Too generic; does not specifically identify the media type problem

**403 Forbidden**
Implies authentication or permission issue, not format rejection

**406 Not Acceptable**
Used when server cannot provide a response in client's accepted format, not for uploaded content

**500 Internal Server Error**
Wrong category; the server is working correctly by rejecting the format

**Client Action:**
The mobile app should read the 415 response, display the allowed formats to the user, and prompt them to select a supported file type before retrying the upload.

**Correct Status Code: 415 Unsupported Media Type**

Server  **415 Unsupported Media Type**  return করবে কারণ uploaded file format server-এর accepted content types violate করে।

**Why 415 is the Right Choice**

**Client error category:**  4xx codes indicate problem client side-এ। Request understood হয়েছে কিন্তু invalid content-এর কারণে process করা যাচ্ছে না।
**Specific to content type:**  415 explicitly signal করে যে server payload accept করছে না কারণ এর media type supported নয়, generic 400-এর বিপরীতে যা সব bad requests cover করে।
**Content-Type header mismatch:**  Client সম্ভবত এমন Content-Type header পাঠিয়েছে (যেমন
```
image/heic
```
বা
```
application/x-bittorrent
```
) যা server document uploads-এর জন্য allow করে না।

**Response Example:**

```
HTTP/1.1 415 Unsupported Media Type
Content-Type: application/json
{
"error": "Unsupported file format",
"message": "Only PDF, JPG, and PNG files are accepted",
"received": "image/webp",
"allowed_types": ["application/pdf", "image/jpeg", "image/png"]
}
```

**Why Not Other Codes?**

Code
Why Incorrect

**400 Bad Request**
Too generic; media type problem specifically identify করে না

**403 Forbidden**
Authentication বা permission issue imply করে, format rejection নয়

**406 Not Acceptable**
Server client-এর accepted format-এ response দিতে না পারলে ব্যবহার হয়, uploaded content-এর জন্য নয়

**500 Internal Server Error**
Wrong category; server correctly format reject করছে

**Client Action:**
Mobile app 415 response পড়বে, user-কে allowed formats দেখাবে, এবং retry করার আগে supported file type select করতে prompt করবে।

☆

3

Previous Question
Combined Bank, AE(IT)/AME, 26

In web technology what do the following status code categories represent? Give some specific example for each. i. 2xx 11. 4xx iii. 5xx

Web_technology
| HTTP Status Code

**HTTP Status Code Categories**
**i. 2xx (Success)**

Indicates that the request was  **successfully received and processed** .
**Example:**  200 OK → Request successful
**Example:**  201 Created → Resource successfully created

**ii. 4xx (Client Error)**

Indicates an  **error from the client side**  (wrong request).
**Example:**  400 Bad Request → Invalid request format
**Example:**  404 Not Found → Requested resource not found

**iii. 5xx (Server Error)**

Indicates an  **error from the server side** .
**Example:**  500 Internal Server Error → Server failed to process request
**Example:**  503 Service Unavailable → Server temporarily unavailable

[Source:Mozilla]

**HTTP Status Code Categories**
**i. 2xx (Success)**

এটি বোঝায় যে request  **সফলভাবে process হয়েছে** ।
**উদাহরণ:**  200 OK → request সফল
**উদাহরণ:**  201 Created → নতুন resource তৈরি হয়েছে

**ii. 4xx (Client Error)**

এটি  **client side error**  নির্দেশ করে (ভুল request)।
**উদাহরণ:**  400 Bad Request → ভুল request format
**উদাহরণ:**  404 Not Found → resource পাওয়া যায়নি

**iii. 5xx (Server Error)**

এটি  **server side error**  নির্দেশ করে।
**উদাহরণ:**  500 Internal Server Error → server error হয়েছে
**উদাহরণ:**  503 Service Unavailable → server সাময়িকভাবে বন্ধ

[Source:Mozilla]

☆

4

Previous Question
BB, AME/AE(IT), 26

Explain HTTP status codes.

Web_technology
| HTTP Status Code

HTTP Status Codes are standard response codes sent by a web server to a client (browser or application) after receiving an HTTP request.
These codes indicate whether the request was successful, failed, redirected, or caused a server error.
HTTP status codes are represented by three-digit numbers.
**Purpose of HTTP Status Codes**

Inform the client about request status.
Help in debugging network or website problems.
Control browser and application behavior.
Support communication between client and server.

**Categories of HTTP Status Codes**
HTTP status codes are divided into five categories:

Status Code Range
Category
Description

100 – 199
Informational
Request received and processing continues

200 – 299
Success
Request completed successfully

300 – 399
Redirection
Further action required

400 – 499
Client Error
Error caused by client request

500 – 599
Server Error
Error occurred on the server

**1. Informational Status Codes (100–199)**
These codes indicate that the request has been received and processing is continuing.

**100 Continue:**  Client can continue sending the request.
**101 Switching Protocols:**  Server agrees to switch protocols.

**2. Success Status Codes (200–299)**
These codes indicate successful request processing.

**200 OK:**  Request completed successfully.
**201 Created:**  New resource created successfully.
**204 No Content:**  Request successful but no content returned.

**3. Redirection Status Codes (300–399)**
These codes indicate that additional action is needed.

**301 Moved Permanently:**  Resource has permanently moved to another URL.
**302 Found:**  Resource temporarily moved.
**304 Not Modified:**  Cached version can be used.

**4. Client Error Status Codes (400–499)**
These errors occur due to problems in the client request.

**400 Bad Request:**  Invalid request syntax.
**401 Unauthorized:**  Authentication required.
**403 Forbidden:**  Access denied.
**404 Not Found:**  Requested resource not found.

**5. Server Error Status Codes (500–599)**
These errors occur when the server fails to process the request.

**500 Internal Server Error:**  General server-side error.
**502 Bad Gateway:**  Invalid response from another server.
**503 Service Unavailable:**  Server temporarily unavailable.
**504 Gateway Timeout:**  Server response timeout.

**Commonly Used HTTP Status Codes**

Status Code
Meaning

200
OK

301
Moved Permanently

400
Bad Request

401
Unauthorized

403
Forbidden

404
Not Found

500
Internal Server Error

503
Service Unavailable

HTTP Status Code হলো standard response code যা web server কোনো HTTP request পাওয়ার পর client (browser বা application)-কে পাঠায়。
এই code দ্বারা বোঝানো হয় request সফল হয়েছে কিনা, ব্যর্থ হয়েছে কিনা, redirect হয়েছে কিনা অথবা server error হয়েছে কিনা।
HTTP status code সাধারণত তিন অংকের সংখ্যা দ্বারা প্রকাশ করা হয়।
**HTTP Status Code-এর উদ্দেশ্য**

Client-কে request-এর অবস্থা জানানো।
Website বা network সমস্যা debugging করতে সাহায্য করা।
Browser এবং application behavior নিয়ন্ত্রণ করা।
Client এবং server-এর মধ্যে communication সহজ করা।

**HTTP Status Code-এর শ্রেণিবিভাগ**
HTTP status code পাঁচটি category-তে বিভক্ত:

Status Code Range
Category
বর্ণনা

100 – 199
Informational
Request গ্রহণ করা হয়েছে এবং processing চলছে

200 – 299
Success
Request সফলভাবে সম্পন্ন হয়েছে

300 – 399
Redirection
অতিরিক্ত action প্রয়োজন

400 – 499
Client Error
Client request-এর কারণে error

500 – 599
Server Error
Server-এর অভ্যন্তরীণ error

**1. Informational Status Codes (100–199)**
এই code বোঝায় request গ্রহণ করা হয়েছে এবং processing চলছে।

**100 Continue:**  Client request পাঠানো চালিয়ে যেতে পারে।
**101 Switching Protocols:**  Server protocol পরিবর্তনে সম্মতি দিয়েছে।

**2. Success Status Codes (200–299)**
এই code বোঝায় request সফলভাবে সম্পন্ন হয়েছে।

**200 OK:**  Request সফল হয়েছে।
**201 Created:**  নতুন resource সফলভাবে তৈরি হয়েছে।
**204 No Content:**  Request সফল কিন্তু কোনো content ফেরত দেয়নি।

**3. Redirection Status Codes (300–399)**
এই code বোঝায় অতিরিক্ত action প্রয়োজন।

**301 Moved Permanently:**  Resource স্থায়ীভাবে অন্য URL-এ সরানো হয়েছে।
**302 Found:**  Resource সাময়িকভাবে অন্যত্র সরানো হয়েছে।
**304 Not Modified:**  Cached version ব্যবহার করা যাবে।

**4. Client Error Status Codes (400–499)**
এই error সাধারণত client request-এর সমস্যার কারণে হয়।

**400 Bad Request:**  Invalid request syntax।
**401 Unauthorized:**  Authentication প্রয়োজন।
**403 Forbidden:**  Access denied।
**404 Not Found:**  Requested resource পাওয়া যায়নি।

**5. Server Error Status Codes (500–599)**
এই error server request process করতে ব্যর্থ হলে ঘটে।

**500 Internal Server Error:**  সাধারণ server-side error।
**502 Bad Gateway:**  অন্য server থেকে invalid response এসেছে।
**503 Service Unavailable:**  Server সাময়িকভাবে unavailable।
**504 Gateway Timeout:**  Server response timeout হয়েছে।

**বহুল ব্যবহৃত HTTP Status Codes**

Status Code
অর্থ

200
OK

301
Moved Permanently

400
Bad Request

401
Unauthorized

403
Forbidden

404
Not Found

500
Internal Server Error

503
Service Unavailable

- ☆

5

Basic

Explain HTTP Status Codes. Why are they important in web communication?

Web_technology
| HTTP Status Code

HTTP Status Codes are three-digit numeric codes returned by a web server to indicate the result of a client's HTTP request. They tell the client whether the request was successful, redirected, invalid, or failed due to a server error. **Importance:** They provide a standard way for clients and servers to communicate, help browsers take appropriate actions, simplify debugging, and improve the reliability of web communication.

HTTP Status Codes হলো Web Server কর্তৃক Client-এর HTTP Request-এর ফলাফল বোঝানোর জন্য ব্যবহৃত তিন সংখ্যার Numeric Code। এগুলো Request সফল হয়েছে, Redirect হয়েছে, Client Error হয়েছে, নাকি Server Error হয়েছে তা নির্দেশ করে। **গুরুত্ব:** এগুলো Client ও Server-এর মধ্যে Standard Communication নিশ্চিত করে, Browser-কে সঠিক Action নিতে সাহায্য করে, Debugging সহজ করে এবং Web Communication আরও নির্ভরযোগ্য করে।

☆

6

Basic

Discuss the role of HTTP Status Codes in client-server communication.

Web_technology
| HTTP Status Code

HTTP Status Codes act as a standard communication mechanism between clients and servers. They indicate the outcome of every HTTP request, allowing browsers and applications to display content, redirect users, or report errors appropriately. They also support efficient troubleshooting and application development.

HTTP Status Codes হলো Client ও Server-এর মধ্যে Standard Communication Mechanism। এগুলো প্রতিটি HTTP Request-এর ফলাফল জানায়, যার মাধ্যমে Browser Webpage প্রদর্শন করে, Redirect করে অথবা Error দেখায়। এছাড়া এগুলো Troubleshooting ও Application Development সহজ করে।

☆

7

Basic

Explain how browsers and web servers use HTTP Status Codes during communication.

Web_technology
| HTTP Status Code

First, the browser sends an HTTP request to the web server. The server processes the request and returns an appropriate HTTP Status Code. The browser interprets the code and performs the required action, such as displaying a webpage, following a redirect, or showing an error message.

প্রথমে Browser একটি HTTP Request Server-এ পাঠায়। এরপর Server Request Process করে একটি HTTP Status Code ফেরত দেয়। Browser সেই Code অনুযায়ী Webpage প্রদর্শন করে, Redirect অনুসরণ করে অথবা Error Message দেখায়।

☆

8

Basic

Differentiate between HTTP 2xx and HTTP 3xx status codes.

Web_technology
| HTTP Status Code

HTTP 2xx status codes indicate that the client's request was successfully received, understood, and accepted by the server. Examples include 200 OK (request successful), 201 Created (resource created), and 204 No Content (successful but no content to return).HTTP 3xx status codes indicate redirection. They inform the client that further action is needed to complete the request, usually by accessing a different URL. Examples include 301 Moved Permanently (resource moved to a new URL permanently), 302 Found (temporary redirect), and 307 Temporary Redirect.

HTTP 2xx Status Codes দেখায় যে Client-এর Request সফলভাবে Server-এর কাছে গ্রহণ করা হয়েছে, বোঝা গেছে এবং Accept করা হয়েছে। উদাহরণ: 200 OK (Request সফল), 201 Created (Resource তৈরি হয়েছে), 204 No Content (সফল কিন্তু কোনো Content নেই)।HTTP 3xx Status Codes দেখায় Redirection। এগুলো Client-কে জানায় যে Request সম্পূর্ণ করতে আরও Action নিতে হবে, সাধারণত অন্য URL-এ যেতে হবে। উদাহরণ: 301 Moved Permanently (স্থায়ীভাবে অন্য URL-এ সরানো), 302 Found (অস্থায়ী Redirect), 307 Temporary Redirect।

☆

9

Basic

Differentiate between HTTP 4xx and HTTP 5xx status codes.

Web_technology
| HTTP Status Code

HTTP 4xx status codes are client error codes. They indicate that the request contains bad syntax or cannot be fulfilled by the server due to a mistake made by the client. Examples include 400 Bad Request, 401 Unauthorized, 403 Forbidden, and 404 Not Found.HTTP 5xx status codes are server error codes. They indicate that the server failed to fulfill a valid request due to an internal server problem. Examples include 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, and 504 Gateway Timeout.

HTTP 4xx Status Codes হলো Client Error Codes। এগুলো দেখায় যে Request-এ Bad Syntax আছে অথবা Client-এর ভুলের কারণে Server Request পূরণ করতে পারছে না। উদাহরণ: 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found।HTTP 5xx Status Codes হলো Server Error Codes। এগুলো দেখায় যে Valid Request হওয়া সত্ত্বেও Server-এর Internal Problem-এর কারণে Request পূরণ করা সম্ভব হয়নি। উদাহরণ: 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout।

☆

10

Basic

Differentiate between HTTP 400 Bad Request and HTTP 404 Not Found.

Web_technology
| HTTP Status Code

HTTP 400 Bad Request indicates that the server cannot process the request because the client sent malformed syntax or an invalid request message. The error is due to incorrect request formatting.HTTP 404 Not Found indicates that the server understood the request but could not find the requested resource at the specified URL. The error is due to the resource not existing on the server.

HTTP 400 Bad Request দেখায় যে Client-এর Request-এ Malformed Syntax বা Invalid Message আছে বলে Server Request Process করতে পারছে না। এটি Request Formatting-এ ভুলের কারণে হয়।HTTP 404 Not Found দেখায় যে Server Request বুঝতে পেরেছে কিন্তু নির্দিষ্ট URL-এ Requested Resource খুঁজে পায়নি। এটি Resource-এর Server-এ না থাকার কারণে হয়।

☆

11

Basic

Differentiate between HTTP 401 Unauthorized and HTTP 403 Forbidden.

Web_technology
| HTTP Status Code

HTTP 401 Unauthorized means the client must authenticate itself to get the requested response. The server requires valid login credentials (username/password or token) that were missing or incorrect.HTTP 403 Forbidden means the server understood the request and the client is authenticated, but the client does not have permission to access the requested resource. Access is denied regardless of authentication.

HTTP 401 Unauthorized মানে Client-কে Response পেতে Authentication করতে হবে। Server Valid Login Credentials (Username/Password বা Token) চায় যা Missing বা Incorrect ছিল।HTTP 403 Forbidden মানে Server Request বুঝতে পেরেছে এবং Client Authenticated, কিন্তু Client-এর Requested Resource-এ Access করার Permission নেই। Authentication থাকা সত্ত্বেও Access Denied।

☆

12

Basic

Differentiate between HTTP 404 Not Found and HTTP 410 Gone.

Web_technology
| HTTP Status Code

HTTP 404 Not Found means the requested resource could not be found on the server, but it does not specify whether the resource was permanently removed or might be available again in the future.HTTP 410 Gone means the requested resource was intentionally and permanently removed from the server, and the server knows it will not be available again. It is more specific than 404.

HTTP 404 Not Found মানে Requested Resource Server-এ পাওয়া যায়নি, কিন্তু এটি নির্দেশ করে না যে Resource স্থায়ীভাবে মুছে ফেলা হয়েছে নাকি ভবিষ্যতে আবার পাওয়া যাবে।HTTP 410 Gone মানে Requested Resource ইচ্ছাকৃতভাবে এবং স্থায়ীভাবে Server থেকে মুছে ফেলা হয়েছে এবং Server জানে যে এটি আর কখনোই পাওয়া যাবে না। এটি 404-এর চেয়ে বেশি Specific।

☆

13

Basic

Differentiate between HTTP 500 Internal Server Error and HTTP 503 Service Unavailable.

Web_technology
| HTTP Status Code

HTTP 500 Internal Server Error is a generic error indicating that the server encountered an unexpected condition that prevented it from fulfilling the request. It usually points to a bug or misconfiguration in the server-side code.HTTP 503 Service Unavailable means the server is currently unable to handle the request due to temporary overload or scheduled maintenance. The server is operational but temporarily unavailable, and the client should retry later.

HTTP 500 Internal Server Error একটি Generic Error যা দেখায় যে Server একটি Unexpected Condition-এর সম্মুখীন হয়ে Request পূরণ করতে পারেনি। এটি সাধারণত Server-side Code-এ Bug বা Misconfiguration-এর কারণে হয়।HTTP 503 Service Unavailable মানে Server বর্তমানে Temporary Overload বা Scheduled Maintenance-এর কারণে Request Handle করতে পারছে না। Server Operational কিন্তু অস্থায়ীভাবে Unavailable, Client-কে পরে Retry করতে হবে।

☆

14

Basic

Differentiate between HTTP 502 Bad Gateway and HTTP 504 Gateway Timeout.

Web_technology
| HTTP Status Code

HTTP 502 Bad Gateway means the server, acting as a gateway or proxy, received an invalid response from an upstream server it accessed to fulfill the request. The upstream server sent a malformed or unexpected response.HTTP 504 Gateway Timeout means the server, acting as a gateway or proxy, did not receive a timely response from the upstream server within the expected time frame. The upstream server took too long to respond.

HTTP 502 Bad Gateway মানে Gateway বা Proxy হিসেবে কাজ করা Server Upstream Server থেকে Invalid Response পেয়েছে। Upstream Server Malformed বা Unexpected Response পাঠিয়েছে।HTTP 504 Gateway Timeout মানে Gateway বা Proxy হিসেবে কাজ করা Server Upstream Server থেকে নির্ধারিত সময়ের মধ্যে Response পায়নি। Upstream Server Response দিতে অনেক বেশি সময় নিয়েছে।

- ☆

15

Scenario Based

A client sends a request to a webpage that no longer exists on the server. Which HTTP status code should be returned? Justify your answer.

Web_technology
| HTTP Status Code

HTTP 404 Not Found should be returned because the requested resource (webpage) does not exist on the server. This status code informs the client that the server could not find the requested page, allowing the browser to display an appropriate error message to the user.

HTTP 404 Not Found Return করা উচিত কারণ Requested Resource (Webpage) Server-এ আর বিদ্যমান নেই। এই Status Code Client-কে জানায় যে Server Requested Page খুঁজে পায়নি, যার মাধ্যমে Browser User-কে উপযুক্ত Error Message দেখাতে পারে।

☆

16

Scenario Based

A user submits a login request without providing authentication credentials. Which HTTP status code should be returned? Explain.

Web_technology
| HTTP Status Code

HTTP 401 Unauthorized should be returned because the request lacks valid authentication credentials. The server requires the user to provide login credentials (such as username/password or an authentication token) before granting access to the protected resource.

HTTP 401 Unauthorized Return করা উচিত কারণ Request-এ Valid Authentication Credentials নেই। Server User-কে Protected Resource-এ Access দেওয়ার আগে Login Credentials (যেমন Username/Password বা Authentication Token) প্রদান করতে বলে।

☆

17

Scenario Based

A logged-in customer attempts to access another customer's confidential banking information without permission. Which HTTP status code should the server return? Explain your answer.

Web_technology
| HTTP Status Code

HTTP 403 Forbidden should be returned because the customer is authenticated (logged in) but does not have the necessary permissions to access another customer's confidential data. The server understands the request but refuses to authorize it due to insufficient privileges.

HTTP 403 Forbidden Return করা উচিত কারণ Customer Authenticated (Logged In) কিন্তু অন্য Customer-এর Confidential Data Access করার Permission নেই। Server Request বুঝতে পেরেছে কিন্তু Insufficient Privileges-এর কারণে এটি Authorize করতে অস্বীকার করেছে।

☆

18

Scenario Based

A client requests a webpage that has been permanently moved to another URL. Which HTTP status code should be returned? Why?

Web_technology
| HTTP Status Code

HTTP 301 Moved Permanently should be returned because the resource has been permanently relocated to a new URL. This status code tells the client (browser) to update its bookmarks and redirect all future requests to the new URL. It also helps with SEO by transferring link equity to the new location.

HTTP 301 Moved Permanently Return করা উচিত কারণ Resource স্থায়ীভাবে নতুন URL-এ সরানো হয়েছে। এই Status Code Client-কে (Browser) জানায় যে Bookmark Update করতে হবে এবং ভবিষ্যতের সব Request নতুন URL-এ Redirect করতে হবে। এটি SEO-তে Link Equity নতুন Location-এ Transfer করতে সাহায্য করে।

☆

19

Scenario Based

Explain how HTTP Status Codes improve communication between clients and web servers.

Web_technology
| HTTP Status Code

HTTP Status Codes provide a standardized language for clients and servers to communicate. They clearly indicate whether a request succeeded, failed, or requires further action. This standardization enables browsers to respond appropriately (display content, redirect, show errors), helps developers debug issues efficiently, and ensures consistent behavior across different systems and platforms.

HTTP Status Codes Client ও Server-এর মধ্যে Standardized Language প্রদান করে। এগুলো স্পষ্টভাবে জানায় যে Request সফল হয়েছে, ব্যর্থ হয়েছে, নাকি আরও Action প্রয়োজন। এই Standardization-এর মাধ্যমে Browser উপযুক্তভাবে Response দেয় (Content প্রদর্শন, Redirect, Error দেখানো), Developers দ্রুত Debug করতে পারে এবং বিভিন্ন System ও Platform-এ Consistent Behavior নিশ্চিত হয়।

☆

20

Scenario Based

Discuss how HTTP Status Codes contribute to security, performance, and maintainability in modern web applications.

Web_technology
| HTTP Status Code

**Security:**  Codes like 401 and 403 enforce authentication and authorization, preventing unauthorized access.  **Performance:**  Codes like 301, 302, and 304 (Not Modified) enable caching and redirection, reducing unnecessary data transfer and server load.  **Maintainability:**  Clear status codes help developers quickly identify and fix issues, monitor application health, and implement proper error handling, making the codebase easier to maintain and scale.

**Security:**  401 এবং 403-এর মতো Codes Authentication ও Authorization প্রয়োগ করে, Unauthorized Access রোধ করে।  **Performance:**  301, 302 এবং 304 (Not Modified)-এর মতো Codes Caching ও Redirection সক্ষম করে, Unnecessary Data Transfer ও Server Load কমায়।  **Maintainability:**  স্পষ্ট Status Codes Developers-কে দ্রুত Issue Identify ও Fix করতে, Application Health Monitor করতে এবং Proper Error Handling Implement করতে সাহায্য করে, যা Codebase Maintain ও Scale করা সহজ করে।

☆

21

Scenario Based

A website is temporarily unavailable because the server is undergoing scheduled maintenance. Which HTTP status code should be returned? Why?

Web_technology
| HTTP Status Code

HTTP 503 Service Unavailable should be returned because it indicates that the server is temporarily unable to handle requests due to maintenance or overload. It informs the client that the unavailability is temporary and the service will be restored soon, allowing clients to retry after some time.

HTTP 503 Service Unavailable Return করা উচিত কারণ এটি দেখায় যে Server Maintenance বা Overload-এর কারণে অস্থায়ীভাবে Request Handle করতে পারছে না। এটি Client-কে জানায় যে Unavailability অস্থায়ী এবং Service শীঘ্রই Restore হবে, যার মাধ্যমে Client কিছুক্ষণ পরে Retry করতে পারে।

☆

22

Scenario Based

A gateway server waits too long for a response from an upstream server before timing out. Which HTTP status code should be returned? Explain.

Web_technology
| HTTP Status Code

HTTP 504 Gateway Timeout should be returned because the gateway or proxy server did not receive a timely response from the upstream server within the allowed time limit. This status code indicates a communication delay between servers, not a client error.

HTTP 504 Gateway Timeout Return করা উচিত কারণ Gateway বা Proxy Server Upstream Server থেকে নির্ধারিত সময়সীমার মধ্যে Response পায়নি। এই Status Code Server-গুলোর মধ্যে Communication Delay নির্দেশ করে, Client Error নয়।

📘 HTTP Status Code

#### 1. What does HTTP stand for?

#### 2. What HTTP method is used when the user first loads a webpage?

#### 3. When is the POST method used?

#### 4. Which HTTP status/response code means success?

#### 5. Which part of the architecture sends a POST request?

#### 6. When is the PATCH method used?

#### 7. When is the DELETE method used?

#### 8. Which HTTP status/response category means Client Errors?

#### 9. Which HTTP status/response category means Redirection?

#### 10. Which status code lets the requesting computer know that the message has been received?

#### 11. What does the HTTP status code 200 indicate?

#### 12. Which HTTP status code represents 'Not Found'?

#### 13. What does the status code 500 represent?

#### 14. Which status code indicates that a request requires user authentication?

#### 15. What does the status code 201 signify?

#### 16. Which of the following are valid HTTP response code categories?

#### 17. HTTP response codes starting with 1xx indicate:

#### 18. What does the HTTP status code 201 (Created) indicate?

#### 19. Which response is received when user authentication has failed?

#### 20. Which response code indicates the new permanent location of the requested resource?

#### 21. When is the HTTP 400 Bad Request response returned?

#### 22. When is the HTTP 502 Bad Gateway response returned?
