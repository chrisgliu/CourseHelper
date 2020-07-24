function readMyDataInput(
    inputs:string[], input_breakdown:string[],
    options:string[], option_breakdown:string[][]){
    let data:{ [input:string]: string; } = {};
    if (options != null) {
        for (let index = 0; index < options.length; index++) {
            const selector = options[index];
            const selector_breakdown = option_breakdown[index];
            let values = getSelectionValue(selector);
            let value_list = readMySessionString(values);
            for (let v_index = 0; v_index < value_list.length; v_index++) {
                const value = value_list[v_index];
                const tag = selector_breakdown[v_index];
                data[tag] = value;
            }  
        }       
    }
    if (inputs != null){
        for (let index = 0; index < inputs.length; index++) {
            const input = inputs[index];
            let value = getInputValue(input);
            let tag = input_breakdown[index];
            data[tag] = value;
        }
    }
    return data;   
}

function getCookie(name:string) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/// django - ajax
function csrfSafeMethod(method:any) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function activateTHISForm(
    submit_button_id:string,
    url_request:string,
    inputs:string[], input_breakdown:string[],
    options:string[], option_breakdown:string[][],
    onclick_update_function:Function
    ) {
        document.getElementById(submit_button_id).onclick = ()=> {
            let json_data =  readMyDataInput(inputs, input_breakdown, options, option_breakdown);
            $.ajax(
                {
                    url:url_request,
                    type:"POST",
                    data:json_data,
                    dataType:"json",
                    beforeSend: function(xhr, settings) {
                        if (!csrfSafeMethod(settings.type)) {
                            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                        }
                    },
                    success: function (){
                        //alert("ok");
                    },
                    error: function (){
                        //alert("no");
                    }
                }
            );
            if (onclick_update_function != null){
                onclick_update_function();
            }
        }
}