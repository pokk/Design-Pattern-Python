Here is a little tips for removing from LogCat tags you don't want to see.

Before I thought I could keep tags what I want but I couldn't find a good way to solve it until now.

All what you need is to click in top right corner of LogCat, select your package name and click *__Edit Filter Configuration__*.

Then in the field called Log Tag regex You have to input this as below:


^(?!.*(MyTag)).*$


which means you don’t want any log which contains dalvivm or OpenGLRenderer. If You want add another word to ignore list just insert inside of regex


|word


For example:


^(?!.*(MyTag|word)).*$


As following the steps, you could filter the tags what you don't want to see.

*__BUT__*, there are still many logs because the system logs, the application logs, bla bla bla.... In any way, so many logs is still there.

Now you just want to see your application's log. You need to click *__Edit Filter Configuration__*.


Then you input your application package name as like
 

'com.my.app.practice'.


You can feel better because you can just see the logs what you want to see.
