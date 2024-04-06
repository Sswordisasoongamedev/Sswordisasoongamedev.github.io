import { add_cookie, getCookieValue, substringsplit, charsplit, logger } from "./cookies.js";

      
        // Now you can use the imported functions
        const username = getCookieValue("Username");
        console.log(username);
        function test(){
            add_cookie("Username = Ssword(dev)")

        }
        function aftest(){
          returned =getCookieValue("Username")
          return returned
        }
        const logger = logger
export { test,aftest,logger }
