<?php
    // Inicia a sessão para poder passar dados entre páginas
    session_start();

    $servername = "localhost";
    $db_username = "sqlinjectionTBB";
    $db_password = "senha@123";
    $dbname = "sqlinjectionTBB";

    $conn = new mysqli($servername, $db_username, $db_password, $dbname);

    if ($conn->connect_error){
        die("Falha na conexão: ". $conn->connect_error);
    }

    if (isset($_POST["username"]) && isset($_POST["password"])){
        $user = $_POST["username"];
        $pass = $_POST["password"];

        $sql = "SELECT * FROM users WHERE name = '$user' AND password = '$pass'";
        $result = $conn->query($sql);

        if (!$result || $result->num_rows == 0) {
            echo "Usuário ou senha Inválido...";
        } else {
            $row = $result->fetch_assoc();

            // CASO ESPECIAL: Login válido e único do H4ck3r
            // A condição num_rows == 1 evita que um bypass revele a flag
            if ($result->num_rows == 1 && $row['name'] === 'H4ck3r' && $row['password'] === 'S3cr3tP@ssw0rdF0rTh3W1n') {
                // Guarda a flag na sessão
                $_SESSION['flag'] = "FLAG{S3SS10N_R1D1NG_F0R_TH3_W1N}";
                // Envia uma resposta de sucesso para o JavaScript
                echo "SUCESSO";
            } else {
                // Para qualquer outro login bem-sucedido (normal ou bypass)
                // Limpa a flag da sessão (caso exista) e envia sucesso
                unset($_SESSION['flag']);
                echo "SUCESSO";
            }
        }
    } else {
        echo "Dados não recebidos...";
    }

    $conn->close();
?>