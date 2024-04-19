function send_cookie(cookie_key_value_pair){
    document.cookie = cookie_key_value_pair+"; path=/";
    /**
     * add a cookie 
     * parameters: >>> cookie_key_value_pair must be separated
     */
}

const logger = console.log;

const title = document.title

add_cookie("Title="+title)