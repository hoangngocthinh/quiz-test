export const showMessage = (status:number|string) : string => {
    let message:string = "";
    switch (status) {
        case 400:
            message = "Bad request";
            break;
        case 401:
            message = "Unauthorized, please log in again";
            break;
        case 403:
            message = "Access denied";
            break;
        case 404:
            message = "Not Found";
            break;
        case 408:
            message = "Request timed out";
            break;
        case 500:
            message = "Server Error";
            break;
        case 501:
            message = "Service not implemented";
            break;
        case 502:
            message = "Network Error";
            break;
        case 503:
            message = "Service is not available";
            break;
        case 504:
            message = "Network timeout";
            break;
        case 505:
            message = "HTTP version not supported";
            break;
        default:
            message = `Connection error (${status})!`;
    }
    return `${message}, please check the network or contact your administrator!`;
};
