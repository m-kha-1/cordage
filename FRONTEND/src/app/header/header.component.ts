import { Component } from '@angular/core';
import { MinLogComponent } from '../min-log/min-log.component';
import { Input } from '@angular/core';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [MinLogComponent],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {
  infoName!:string | null;
  infoRole!:string | null;
   
  
   ngOnInit() { this.infoName= localStorage.getItem('userName');
    this.infoRole= localStorage.getItem('userType')


   
  }
}
