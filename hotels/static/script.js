
$( document ).ready(function() {
  console.log('Debug');
   
    $("#country_select").change(function () {
      ajaxFunc();
    });
    $('#sorting').change(function () { ajaxFunc(); 
    });
       
});

function ajaxFunc() { 
      var country_id = $('#country_select').val();
      var sorting = $('#sorting').val();  
      $.ajax({
        url: 'ajax/hotel/',
        data: {
          'country_id': country_id,
          'sorting': sorting
        },
        dataType: 'json',
        success: function (data) {
          if (data.hotels) {
            console.log(data.hotels);
            genHotels(data.hotels)
          }
        }
      });
}

function genHotels(hotels) {
        
    var div_list_of_hotels = document.getElementById('list_of_hotels');
    //очищаем див с отелями
    while(div_list_of_hotels.firstChild){
        div_list_of_hotels.removeChild(div_list_of_hotels.firstChild);
        }
              
    for (var i = 0; i < hotels.length; i++) {
        //создаем ноды
        var main_node = document.createElement("div");
        var name_node = document.createElement("div");
        var price_node = document.createElement("div");
        
        main_node.classList.add('hotel-cube');
        name_node.classList.add('name');
        price_node.classList.add('price');
                
        name_node.title = hotels[i][0]
        main_node.style.backgroundImage = "url('media/"+hotels[i][2]+"')";
        
        //добавляем текстовые ноды        
        var textnode = document.createTextNode(hotels[i][0]);  
        name_node.appendChild(textnode);
        textnode = document.createTextNode(hotels[i][1]); 
        price_node.appendChild(textnode);
        // собираем все внутри ноды отеля
        main_node.appendChild(name_node);
        main_node.appendChild(price_node);
        //добавляем див с отелем
        div_list_of_hotels.appendChild(main_node);   
            }
    }


