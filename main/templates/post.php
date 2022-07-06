<?php
    include_once ("admin/classes/Database.php");
    $db = new classes\Database;
    if(isset($_REQUEST['blog']) && isset($_REQUEST['id']) && $_REQUEST['blog']!= '' && $_REQUEST['id']!=''){
    $id = $_REQUEST['id'];
    $sel_blog_post = $db->select("SELECT * FROM `blog` WHERE `id`='$id'");
    $post = $sel_blog_post->fetch_assoc();
    if($post){
    $title = $post['title'];
    include ("inc/header_one.php");
?>
<section id="post" class="mtop">
    <div class="container">
        <div class="post-con">
            <h2 class="text-center my-4 clearfix d-block"><?= $post['title'] ?></h2>
            <div class="post_img mb-4">
                <img class="" src="<?= $dir.$post['image'] ?>" alt="">
            </div>
            <p><?= $post['blg_dsc'] ?></p>
        </div>
    </div>
</section>

<?php
    include ("inc/footer.php");
    }else{
        echo "Sorry someting want wrong";
    }
}
?>