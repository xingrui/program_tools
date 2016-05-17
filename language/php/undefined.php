<?php
    function sendMail($subject, $message) {
        $content = Array();
        $content['subject'] = $subject;
        $content['message'] = $message;
        var_dump($content);
        $postData = http_build_query($content);
        $options = array(
            'http' => array(
                'method' => 'POST',
                'header' => 'Content-type: application/x-www-form-urlencoded',
                'content' => $postData,
            ),
        );
        $context = stream_context_create($options);
        $url = 'http://mobmail.mobvista.com/jackson/mail.php';
        $result = file_get_contents($url, false, $context);
        var_dump($result);
    }

$exception = new Exception();
$error_msg = "Catch unknown exception when offline detect. Excetion:" . $exception . message;
var_dump($error_msg);
sendMail('click_opt', $error_msg);
