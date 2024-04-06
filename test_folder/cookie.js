import { add_cookie, getCookieValue, substringsplit, charsplit } from ".cookies.js";

      
        // Now you can use the imported functions
        const username = getCookieValue("Username");
        console.log(username);
        function test(){
            add_cookie("Username = Ssword(dev)")
        }