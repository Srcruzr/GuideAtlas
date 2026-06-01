// Menús principales

const mainButtons = document.querySelectorAll(".dropdown-main");

mainButtons.forEach(button => {

    button.addEventListener("click", () => {

        const menu = button.nextElementSibling;

        if(menu.style.display === "block"){

            menu.style.display = "none";

        }else{

            menu.style.display = "block";

        }

    });

});


// Menús de cada mundo

const worldButtons = document.querySelectorAll(".dropdown-world");

worldButtons.forEach(button => {

    button.addEventListener("click", () => {

        const worldMenu = button.nextElementSibling;

        if(worldMenu.style.display === "block"){

            worldMenu.style.display = "none";

        }else{

            worldMenu.style.display = "block";

        }

    });

});