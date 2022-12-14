# Spécialité NSI en Première

Télécharger le [starter code](docs/../site_web.zip)

## Introduction

Le but de ce site web est de vous proposer un cours interactif **à travailler à la maison** : vous pourrez programmer en Python en ligne sans avoir besoin d'installer un éditeur.

Je vous conseille d'utiliser le navigateur **Firefox**, **Chrome** ou **Chromium** afin de bénéficier de la meilleure expérience utilisateur.

Comme toute langue, la programmation s'apprend avant tout en lisant, en écrivant, en répétant et en s'entrainant. Ainsi, le copier/coller des commandes Python de ce cours a été désactivé. Pour les tester, vous allez devoir les écrire !

De nombreux exercices **corrigés** vous sont également proposés : faites-les tous, préparez les questions que nous traiterons en cours et vous réussirez les interrogations de début de cours.

Ce site respecte votre vie privée : aucun cookie n'est demandé ; aucune inscription n'est requise.

## Fonctionnement des exercices

Trois grands types d'exercices sont proposés.

!!! example "Papier/Crayon"

    Pas de problème. Prenez une feuille et un crayon. Ne trichez pas en regardant la correction trop vite.

!!! example "Prédire/comprendre"

    Comme ci-dessous, vous disposez d'un programme dans un éditeur. Vous devez comprendre le programme et prédire ce qui va se passer. Vous pouvez tester en appuyant sur la flèche pointant à droite.
            <p>Status: <span id="status">Disconnected.</span></p>
			        <div id="content">
            Please connect your Numworks.
        </div>
    {{IDE('intro')}}

!!! example "Programmer"

    Vous devez compléter ou écrire un programme dans un éditeur. 

    - Vous pouvez tester en appuyant sur la flèche pointant à droite ▶️. 
    - Vous pouvez tenter de valider votre programme pour savoir si celui-ci est correct en cliquant sur le gendarme 🛂. Votre programme est alors soumis à de nombreux tests. 
    - Au bout de 5 validations ratées, la solution apparait.

    {{IDE('exo2')}}

## FAQ

Voici quelques questions que ous pourriez vous poser :

!!! help "Rien ne s'enregistre et lorsque je recharge la page internet, tout s'efface !"

    C'est normal. Il n'y a pas de cookie ou de sessions. Vos données ne sont donc pas enregistrées.

    Vous pouvez toutefois télécharger vos programmes lorsque ceux-ci sont importants.

!!! help "C'est normal que je n'arrive pas à faire un copier/coller de certains codes du cours ?"

    Oui. J'ai bloqué cette fonctionnalité. La programmation s'apprend en programmant.

!!! help "Il faut vraiment TOUT savoir ce qu'il y a sur votre site ?"

    Non. Avec le  contrôle de cours, je m'assure que vous avez travaillé le cours avant de venir. Sinon, vous perdez votre temps et celui de vos camarades.

!!! help "Un contrôle de cours par semaine, ça sert à rien et ça fait perdre du temps."

    Non. Avec un contrôle de cours, je m'assure que vous avez travaillé le cours avant de venir. Sinon, vous perdez votre temps et celui de vos camarades.

!!! help "C'est sympa de pouvoir coder directement sur une page web. Qui est responsable de cela ?"

    C'est moi qui ait développé tout le moteur. Cela fonctionne grâce à une technologie de 2017 appelé WebAssembly. Celle-ci permet de coupler Javascript et Python. Et d'autres développements arrivent...

<script src="javascripts/numworks.js"></script>

<script>
var editor = ace.edit("editor_1");
var code = editor.getValue();


var calculator = new Numworks();

var status = document.getElementById("status");
var connect = document.getElementById("connect");
var content = document.getElementById("content");

navigator.usb.addEventListener("disconnect", function(e) {
  calculator.onUnexpectedDisconnect(e, function() {
    status.innerHTML = "Disconnected.";
    content.innerHTML = "Please connect your Numworks.";
    calculator.autoConnect(autoConnectHandler);
  });
});

function handleScriptSend(type) {
    var editor = ace.edit(type);
    var code = editor.getValue();
    connected(code, "mkdocs", 1);
}
	
calculator.autoConnect(autoConnectHandler);

function autoConnectHandler(e) {
  calculator.stopAutoConnect();
  code = editor.getValue();
  connected("", "", 0);      
}

connect.onclick = function(e) {
  calculator.detect(function() {
    calculator.stopAutoConnect();
    connected("","",0);
  }, function(error) {
    status.innerHTML = "Error: " + error;
  });
};

async function connected(script, name, send) {
  connect.disabled = true;
  status.innerHTML = "Connected.";

  var model = calculator.getModel(false);

  var html_content = "Model: " + calculator.getModel(false) + "<br/>";

  // Get the platform information
  var platformInfo = await calculator.getPlatformInfo();
  console.log(platformInfo);
  if(send) {
  var storage = await calculator.backupStorage();
	storage.records.push({"name": name, "type": "py", "autoImport": true, position: 0, "code": script});
	await calculator.installStorage(storage, function() {
    console.log("don")
	});
  }
  content.innerHTML = html_content;
}
</script>
