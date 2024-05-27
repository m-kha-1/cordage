import { Component } from '@angular/core';
import { ProductionsService } from '../productions.service';

import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  username!: string;
  password!: string;
  test:any;

  constructor(private productionsService: ProductionsService,private router: Router) { }


    
  
  onSubmit() {
    this.productionsService.login(this.username, this.password).subscribe(
      data => {
        // Traitement en cas de succès de la connexion
        console.log('Connecté avec succès', data);
        this.router.navigate(['/productions']);
      },
      error => {
        // Traitement en cas d'échec de la connexion
        console.error('Erreur de connexion', error);
      }
 
    );
   


  }

  
  


}