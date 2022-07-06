<?php
    include_once ("admin/classes/Database.php");
    $db = new classes\Database;
    $title = "Client Review";
    include ("inc/header_one.php");
?>
<section id="review">
    <div class="container">
        <div class="review-con text-center">
            <h1 class="review-title">customer review</h1>
            <div class="row">
                <?php
                    $sel_test = $db->select("SELECT * FROM `review`");
                    while($test = $sel_test->fetch_assoc()){
                ?>
                <div class="col-md-3 mb-4">
                    <div class="review-div">
                        <div class="customer-img mb-4">
                            <img class="img-fluid" src="<?= $dir.$test['clnt_img'] ?>" alt="Customer porfile image">
                        </div>
                        <table class="customer-dtl table table-borderless text-sm-left">
                            <tbody>
                                <tr>
                                    <td>Name:</td>
                                    <td><?= $test['clnt_name'] ?></td>
                                </tr>
                                <tr>
                                    <td>Comment:</td>
                                    <td class="comm"><div class="cstm-comm"><?= $test['clnt_cmnt'] ?></div></td>
                                </tr>
                                <tr>
                                    <td>Country:</td>
                                    <td><strong><?= $test['clnt_cntry'] ?></strong></td>
                                </tr>
                                <tr>
                                    <td>Review:</td>
                                    <td class="rating"><?= $test['clnt_rting'] ?> <i class="fas fa-star"></i></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <?php } ?>
            </div>
        </div>
    </div>
</section>
<?php 
    include ("inc/footer.php");
?>