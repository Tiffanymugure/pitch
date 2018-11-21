from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitches, Comments, PitchListing
from .forms import UpdateProfile, PitchForm, CommentForm, ListingForm
from .. import db, photos


@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Welcome to the Pitching site'
    pitch = Pitches.query.all()

    return render_template('index.html', title=title, pitch=pitch)


# Route for adding a new pitch

@main.route('/listing/pitch/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
    '''
    Function to check Pitches form
    '''
    form = PitchForm()
    listing = PitchListing.query.filter_by(id=id)

    if listing is None:
        abort(404)

    if form.validate_on_submit():
        pitchess = Pitches(actual_pitch=form.content.data, listing=form.category.data)
        pitchess.save_pitch()
    
        return redirect (url_for('main.index'))
    return render_template('new_pitch.html', pitch_form=form)

# Routes for displaying the different pitches
@main.route('/listing/new',methods=['GET','POST'])
@login_required
def new_listing():
	form = ListingForm()
	if form.validate_on_submit():
		name = form.add.data
		new_listing = PitchListing(name=name)
		new_listing.save_listing()
		return redirect(url_for('main.index'))
	title = 'New Pitch Listing'
	return render_template('new_listing.html',listing_form=form)

@main.route('/listing/<int:id>')
def listing(id):
    '''
    listing route function returns a list of pitches in the listing chosen
    '''

    listing = PitchListing.query.get(id)
    if listing is None:
        abort(404)

    # pitches = Pitches.get_pitches(id)
    return redirect (url_for('main.index'))
    return render_template('listing.html', listing=listing, )


@main.route('/comment',methods = ['GET','POST'])
def comment():
    '''
    comment route function returns a list of  in the listing chosen
    '''
    form = CommentForm()
    comments = Comments.query.all()
    if comment is None:
        abort(404)
    if form.validate_on_submit():
        description = form.description.data
        new_comment = Comments(actual_comment = description)
        db.session.add(new_comment)
        db.session.commit()
    return render_template('comment.html', comments=comments , form = form)


@main.route('/pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def single_pitch(id):
    '''
    Function the returns a single pitch for comment to be added
    '''
    pitches = PitchForm()

    if pitches.validate_on_submit():

        pitchess = Pitches(pitch=pitches.pitch.data, listing=pitches.listing.data)
        pitchess.save_pitch()
        return redirect(url_for('listing'))

    # if pitches is None:
    #     abort(404)

    comment = Comments.get_comments(id)
    return redirect (url_for('main.index'))
    return render_template('pitch.html', pitch=pitches, comment=comment)


# Routes for user authentication
@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

# Route to add commments.


@main.route('/pitch/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    '''
    Function that returns a list of comments for the particular pitch
    '''
    form = CommentForm()
    pitches = Pitches.query.filter_by(id=id).first()
    print(pitches.listing)

    if pitches is None:
        abort(404)

    if form.validate_on_submit():
        comment = form.description.data
        new_comment = Comments(user_id=current_user.id, comment_id=comment, pitches_id=pitches.id)
        new_comment.save_comment()
        return redirect(url_for('main.listing', id=pitches.id))

    return render_template('comment.html', comment_form=form)



# Pitch Listing
@main.route('/business', methods = ['GET', 'POST'])
def business():
    """
    displaying business pitches
    """
    business=Pitches.query.filter_by(listing="Business").all()
    return redirect (url_for('main.index',))
    return render_template('buinsess.html', pitches =business)

@main.route('/entertainment', methods = ['GET', 'POST'])
def entertainment():
    """
     show entertainment pitches
    """
    entertainment = Pitches.query.filter_by(listing="Entertainment").all()

    return render_template('Entertainment.html', pitches=entertainment)


@main.route('/comedy', methods = ['GET', 'POST'])
def comedy():
    """
    show comedy pitches
    """
    comedy = Pitches.query.filter_by(listing='comedy').all()

    return render_template('comedy.html', pitches=comedy)


# @main.route('/like/<id>')
# @login_required
# def like(id):
# 	if Likes.query.filter(Likes.users_id==current_user.id,Likes.post_id==id).first():
# 		return url_for('main.new_pitch',id=Likes.post_id)
# 	Likes(users_id=current_user.id).save()
# 	return url_for('main.new_pitch',id=Likes.post_id)

# @main.route('/dislike/<id>')
# @login_required
# def dislike(id):
# 	if Dislikes.query.filter(Dislikes.users_id==current_user.id,Dislikes.post_id==id).first():
# 		return url_for('main.new_pitch',id=Dislikes.post_id)
# 	Dislikes(users_id=current_user.id,post_id=id).save()
# 	return url_for('main.new_pitch',id=Dislikes.post_id)