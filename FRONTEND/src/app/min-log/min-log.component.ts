import { Component } from '@angular/core';
import { ProductionsService } from '../productions.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-min-log',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './min-log.component.html',
  styleUrl: './min-log.component.css'
})
export class MinLogComponent {
  username!: string;
  password!: string;
  constructor(private productionsService: ProductionsService,private router: Router) { }
  onSubmit(){
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
