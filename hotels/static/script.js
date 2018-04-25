
$( document ).ready(function() {
    $("#country_select").change(function () {
      var country_id = $(this).val();
      $.ajax({
        url: 'ajax/hotel/',
        data: {
          'country_id': country_id
        },
        dataType: 'json',
        success: function (data) {
          if (data.hotels) {
            genHotels(data.hotels)
          }
        }
      });

    });
});
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
                
        name_node.title = hotels[i].name
        main_node.style.backgroundImage = "url('media/"+hotels[i].image+"')";
        
        //добавляем текстовые ноды        
        var textnode = document.createTextNode(hotels[i].truncated_name);  
        name_node.appendChild(textnode);
        textnode = document.createTextNode(hotels[i].price); 
        price_node.appendChild(textnode);
        // собираем все внутри ноды отеля
        main_node.appendChild(name_node);
        main_node.appendChild(price_node);
        //добавляем див с отелем
        div_list_of_hotels.appendChild(main_node);   
            }
    }


