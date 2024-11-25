# model adoption
# src/setup_db_example/models/m_adoption.py

from src.setup_db_example.database import db

class AdoptionDb(db.Model):
    __tablename__ = "adoption_db_tbl"

    adoption_id = db.Column(db.Integer, primary_key=True)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppy_db_tbl.puppy_id'), nullable=False)
    owner_id = db.Column(db.Integer, nullable=True)  # Nullable
    date_adopted = db.Column(db.Date, nullable=True)  # Nullable

    puppy = db.relationship("PuppyDb", back_populates="puppy_adopt")




# API adoption
# src/setup_db_example/routes/adoption.py

from flask import Blueprint, request
from src.setup_db_example.database import db
from src.setup_db_example.models.m_adoption import AdoptionDb
import traceback

adoption_db_router = Blueprint("a_adoption", __name__)

# Add Adoption
@adoption_db_router.route("/api/adopt-puppy", methods=["POST"])
def adopt_puppy():
    req = request.json["params"]
    try:
        puppy_id = req["puppy_id"]

        new_adoption = AdoptionDb(
            puppy_id=puppy_id,
            owner_id=None,  # Initially set to None
            date_adopted=None,  # Initially set to None
        )
        db.session.add(new_adoption)
        db.session.commit()
        return {
            "success": True,
            "message_response": "ADOPTION REGISTERED SUCCESSFULLY",
            "message_content": "Adoption Added",
        }
    except Exception as e:
        print(traceback.format_exc())
        return {
            "success": False,
            "message_response": "ADOPTION ADD FAILED",
            "message_content": "Adding Failed",
        }

# Update Adoption
@adoption_db_router.route("/api/update-adoption/<int:adoption_id>", methods=["PUT"])
def update_adoption(adoption_id):
    req = request.json["params"]
    try:
        adoption_record = AdoptionDb.query.get(adoption_id)
        if not adoption_record:
            return {
                "success": False,
                "message_response": "ADOPTION NOT FOUND",
                "message_content": "No adoption record found with this ID",
            }, 404

        # Update owner_id and date_adopted from the request
        adoption_record.owner_id = req.get("owner_id")
        adoption_record.date_adopted = req.get("date_adopted")

        db.session.commit()
        return {
            "success": True,
            "message_response": "ADOPTION UPDATED SUCCESSFULLY",
            "message_content": "Adoption Updated",
        }
    except Exception as e:
        print(traceback.format_exc())
        return {
            "success": False,
            "message_response": "ADOPTION UPDATE FAILED",
            "message_content": "Updating Failed",
        }
        



# model owner
# src/setup_db_example/routes/owner.py

from flask import Blueprint, request
from src.setup_db_example.database import db
from src.setup_db_example.models.m_owner import OwnerDb
import traceback

owner_db_router = Blueprint("a_owner", __name__)

# Register Owner
@owner_db_router.route("/api/register-owner", methods=["POST"])
def register_owner():
    req = request.json["params"]
    try:
        owner_name = req["owner_name"]
        owner_contact_number = req["owner_contact_number"]
        owner_address = req["owner_address"]

        new_owner = OwnerDb(
            owner_name=owner_name,
            owner_contact_number=owner_contact_number,
            owner_address=owner_address,
        )
        db.session.add(new_owner)
        db.session.commit()
        return {
            "success": True,
            "message_response": "OWNER REGISTERED SUCCESSFULLY",
            "message_content": "Owner Added",
            "owner_id": new_owner.owner_id,  # Return the new owner ID
        }
    except Exception as e:
        print(traceback.format_exc())
        return {
            "success": False,
            "message_response": "OWNER REGISTRATION FAILED",
            "message_content": "Registration Failed",
        }