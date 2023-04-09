// https://github.com/RobinHerbots/Inputmask (saved for future reference)

$(document).ready(function () {
    $(".mask-phone").inputmask("(99) 9 9999-9999", { jitMasking: true });
    $("#id_cpf").inputmask("999.999.999-99", { jitMasking: true });
    $(".vDateField").inputmask("99/99/9999", { jitMasking: true });
    $(".vTimeField").inputmask("99:99:99", { jitMasking: true });
});