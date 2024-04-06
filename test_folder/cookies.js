const cookies = document.cookie;
export function add_cookie(cookie_key_value_pair){
    document.cookie = cookie_key_value_pair;
    /**
     * add a cookie 
     * parameters: >>> cookie_key_value_pair must be separated
     */
}
logger =console.log;
export function getCookieValue(cookieKey) {
    // Split the document.cookie string into an array of individual cookies
    var cookiesArray = document.cookie.split(';');
  
    // Loop through each cookie to find the one with the specified key
    for (var i = 0; i < cookiesArray.length; i++) {
        var cookie = cookiesArray[i];

        cookie = cookie.trim();
        // Check if this cookie starts with the desired key
        if (cookie.indexOf(cookieKey + '=') === 0) {
            // Extract and return the value of the cookie
            return cookie.substring(cookieKey.length + 1);
        }
    }
    // Return null if the cookie is not found
    return null;
}
export function substringsplit(str){
    const str_splitted = str.split(" ")
    return str_splitted
}
export function charsplit(str){
    var char_splitted = [];
    for(let k = 0; k < str.length; k++){
        char_splitted.push(str[k]);
    }
    return char_splitted;
}



export { charsplit, add_cookie, getCookieValue, substringsplit };