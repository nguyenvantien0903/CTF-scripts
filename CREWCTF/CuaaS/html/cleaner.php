<?php

if ($_SERVER["REMOTE_ADDR"] != "127.0.0.1"){

die("<img src='https://imgur.com/x7BCUsr.png'>");

}


echo "<br>There your cleaned url: ".$_POST['host'];
echo "<br>Thank you For Using our Service!";


function tryandeval($value){
                echo "<br>How many you visited us ";
                echo $value;
                eval($value);
        }


foreach (getallheaders() as $name => $value) {
	if ($name == "X-Visited-Before"){
		tryandeval($value);
	}}
?>
disable_functions = proc_open, popen, disk_free_space, diskfreespace, set_time_limit, leak, tmpfile, exec, system, passthru, show_source, system, phpinfo, pcntl_alarm, pcntl_fork, pcntl_waitpid, pcntl_wait, pcntl_wifexited, pcntl_wifstopped, pcntl_wifsignaled, pcntl_wexitstatus, pcntl_wtermsig, pcntl_wstopsig, pcntl_signal, pcntl_signal_dispatch, pcntl_get_last_error, pcntl_strerror, pcntl_sigprocmask, pcntl_sigwaitinfo, pcntl_sigtimedwait, pcntl_exec, pcntl_getpriority, pcntl_setpriority