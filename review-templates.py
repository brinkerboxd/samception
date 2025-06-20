import json

with open('users.json','r') as f:
    ftext = f.read()
entries = json.loads(ftext)
review_list = ""
for i in entries:
    user = i["user"]
    stars= i["stars"]
    time_format_one = i["time_format_one"]
    time_format_two = i["time_format_two"]
    rating_color = i["rating_color"]
    review_text = i["review_text"]
    review = f"""
                            <div class="listitem"> <article class="production-record -viewing" data-js-treasure-hunt="index-target"> <a class="avatar -a40" href="https://brinkerboxd.github.io/samception/a.ltrbxd.com/resized/avatar/upload/{user}.jpg"> <img src=""../../../a.lttrboxd.com/resized/avatar/upload/{user}.png" alt="{user}" width="40" height="40"> </a> <div class="body"> <div class="content-reactions-strip -viewing"> <span class="rating -{rating_color} rated-{stars}"> &#9733;&#9733;&#9733;&#9733;&#189; </span> <span class="inlineicon icon-16 -ignoreactionpseudo icon-liked -hidelabel"><span class="icon" role="presentation"></span><span class="label">Liked</span></span> <span class="attribution-detail"> <a href="https://brinkerboxd.github.io/{user}/film/samception/" class="context"> Watched by <span class="owner"><strong class="displayname">{user}</strong></span> </a> </span> <span class="date"> <time class="timestamp" datetime="{time_format_one}">{time_format_two}</time> </span> <a href="https://brinkerboxd.github.io/{user}/film/samception/#comments" class="inlineicon icon-16 -ignoreactionpseudo icon-comment"><span class="icon" role="presentation"></span><span class="label">34</span></a> </div> <div class="js-review "> <div class="body-text -prose js-review-body js-collapsible-text" data-full-text-url="/s/full-text/viewing:107816262/" data-is-translatable="true" lang="en"> <p>{review_text}</p> </div> <div class="viewing-actions"> <div class="review-actions"> <p class="like-link-target react-component" data-component-class="globals.comps.LikeComponent" data-likeable-uid="viewing:107816262" data-likeable-name="review" data-likeable-type="viewing" data-likeable="true" data-element-type="p" data-likes-page="/{user}/film/samception/likes/" data-format="count" data-count="17462" data-owner="{user}"> <span class="has-icon icon-16 icon-like"></span> </p> <button hidden class="translation-button button -text" data-translation-control-for="1aXRlH"> <span class="label js-label">Translate</span> </button> <div hidden class="translation-disclaimer js-translation-disclaimer"> Translated from <span class="js-language-name"></span> by <span class="js-translated-by"></span> </div> </div> </div> </div> </div> </article> </div>
    """
    review_list+= review
    review_list += '\n'
with open('reviews.html','w') as f:
    f.write(review_list)

# """
# example json
# {'user' : 'aaron-gladstone',
# 'date':'',
# 'image_path':'',
# 'stars':'',
# 'text':''
# }
# """

# '''
# <div class="listitem"> 
#     <article class="production-record -viewing" data-js-treasure-hunt="index-target">
#      <a class="avatar -a40" href="https://brinkerboxd.github.io/ksenijab/"> <img src="../../../../../../a.ltrbxd.com/resized/avatar/upload/1/5/9/4/5/9/7/shard/avtr-0-80-0-80-crop_v_a1c4ea4f0d.jpg" alt="ksenija" width="40" height="40"> </a> <div class="body"> <div class="content-reactions-strip -viewing"> <span class="rating -green rated-9"> &#9733;&#9733;&#9733;&#9733;&#189; </span> <span class="inlineicon icon-16 -ignoreactionpseudo icon-liked -hidelabel"><span class="icon" role="presentation"></span><span class="label">Liked</span></span> <span class="attribution-detail"> <a href="https://brinkerboxd.github.io/ksenijab/film/samception/" class="context"> Watched by <span class="owner"><strong class="displayname">ksenija</strong></span> </a> </span> <span class="date"> <time class="timestamp" datetime="2020-05-31">{time_format_two}</time> </span> <a href="https://brinkerboxd.github.io/ksenijab/film/samception/#comments" class="inlineicon icon-16 -ignoreactionpseudo icon-comment"><span class="icon" role="presentation"></span><span class="label">34</span></a> </div> <div class="js-review "> <div class="body-text -prose js-review-body js-collapsible-text" data-full-text-url="/s/full-text/viewing:107816262/" data-is-translatable="true" lang="en"> <p>christopher nolan spent years writing this movie's complex plot and really named the main character dom cobb</p> </div> <div class="viewing-actions"> <div class="review-actions"> <p class="like-link-target react-component" data-component-class="globals.comps.LikeComponent" data-likeable-uid="viewing:107816262" data-likeable-name="review" data-likeable-type="viewing" data-likeable="true" data-element-type="p" data-likes-page="/ksenijab/film/samception/likes/" data-format="count" data-count="17462" data-owner="ksenijab"> <span class="has-icon icon-16 icon-like"></span> </p> <button hidden class="translation-button button -text" data-translation-control-for="1aXRlH"> <span class="label js-label">Translate</span> </button> <div hidden class="translation-disclaimer js-translation-disclaimer"> Translated from <span class="js-language-name"></span> by <span class="js-translated-by"></span> </div> </div> </div> </div> </div> </article> </div>
# '''



