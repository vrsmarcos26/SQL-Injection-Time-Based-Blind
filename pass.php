<?php
    // Inicia a sessão para ler os dados guardados pelo login.php
    session_start();
?>
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Acesso Permitido</title>
        <style>
            body { font-family: sans-serif; background-color: #f0f8ff; text-align: center; padding-top: 100px; }
            .container { background: white; padding: 30px; display: inline-block; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h3 { color: #333; }
            p { color: #666; }
            .flag { color: #28a745; font-weight: bold; font-size: 1.2em; margin-top: 20px; }
        </style> 
    </head>
    <body>
        <div class="container">
            <h3>Onde está minha flag?</h3>
            <p>Acho que minha flag não está aqui...</p>
            <p>Talvez você precise de um acesso mais específico.</p>
            
            <?php
                // Verifica se a flag foi definida na sessão pelo login.php
                if (isset($_SESSION['flag'])) {
                    // Se a flag existe, exibe-a!
                    echo '<p class="flag">Parabéns! Você encontrou: ' . htmlspecialchars($_SESSION['flag']) . '</p>';
                    // Limpa a flag da sessão para que não apareça novamente
                    unset($_SESSION['flag']);
                }
            ?>
        </div>
    </body>
</html>