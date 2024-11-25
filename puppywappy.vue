<template>
  <div>
    <h2>Register Owner</h2>
    <form @submit.prevent="registerOwner">
      <div class="form-group">
        <label for="ownerId">Owner ID:</label>
        <input
          v-model="ownerForm.owner_id"
          type="number"
          id="ownerId"
          required
        />
      </div>
      <div class="form-group">
        <label for="adoptionId">Adoption ID:</label>
        <input
          v-model="ownerForm.adoption_id"
          type="number"
          id="adoptionId"
          required
        />
      </div>
      <div class="form-actions">
        <button type="submit" class="btn btn-primary">Register Owner</button>
      </div>
    </form>
  </div>
</template>

<script>
import { FetchAPI } from "@/components/utility/apiRequest";
export default {
  name: "OwnerRegister",
  data() {
    return {
      ownerForm: {
        owner_id: null,
        adoption_id: null,
      },
    };
  },
  methods: {
    async registerOwner() {
      try {
        // Code to register owner goes here

        // After successful registration, update the adoption record
        const response = await new FetchAPI().put(
          `/api/update-adoption/${this.ownerForm.adoption_id}`,
          {
            params: {
              owner_id: this.ownerForm.owner_id,
              date_adopted: new Date().toISOString().split("T")[0], // Set the current date as the date adopted
            },
          }
        );

        if (response.success) {
          alert("Owner registered and adoption updated successfully!");
        } else {
          alert("Failed to update adoption record.");
        }
      } catch (error) {
        console.error("Error registering owner:", error);
        alert("An error occurred while registering the owner.");
      }
    },
  },
};
</script>



-----------------------------------------------------------


<template>
    <div>
      <h2>Register Owner</h2>
      <form @submit.prevent="registerOwner">
        <div class="form-group">
          <label for="ownerName">Owner Name:</label>
          <input v-model="ownerForm.owner_name" type="text" id="ownerName" required />
        </div>
  
        <div class="form-group">
          <label for="ownerContactNumber">Contact Number:</label>
          <input v-model="ownerForm.owner_contact_number" type="text" id="ownerContactNumber" required />
        </div>
  
        <div class="form-group">
          <label for="ownerAddress">Address:</label>
          <input v-model="ownerForm.owner_address" type="text" id="ownerAddress" required />
        </div>
  
        <div class="form-actions">
          <button type="submit" class="btn btn-primary">Register Owner</button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import { FetchAPI } from '@/components/utility/apiRequest'
  export default {
    name: 'OwnerRegister',
    data() {
      return {
        ownerForm: {
          owner_name: '',
          owner_contact_number: '',
          owner_address: '',
        },
      }
    },
    methods: {
      async registerOwner() {
        try {
          const response = await new FetchAPI().post('/api/register-owner', {
            params: this.ownerForm,
          });
  
          if (response.success) {
            alert("Owner registered successfully!");
            // Optionally, you can also update the adoption record here
            // For example, you can call the update adoption API with the new owner ID.
            // this.updateAdoption(response.owner_id);
          } else {
            alert("Owner registration failed.");
          }
        } catch (error) {
          console.error("Error registering owner:", error);
          alert("An error occurred while registering the owner.");
        }
      },
      async updateAdoption(owner_id) {
        // You can implement this method to update the adoption record
        // after the owner has been successfully registered.
      },
    },
  }
  </script>
