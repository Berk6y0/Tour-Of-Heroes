import { Routes } from '@angular/router';
import { HeroesComponent } from './heroes/heroes.component';
import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { HeroDetailComponent } from './hero-detail/hero-detail.component';

export const routes: Routes = [
 
    {path:'heroes',component:HeroesComponent},
    { path: '', component: DashboardComponent },
    { path: 'dashboard', component: DashboardComponent },
    {path:'detail/:id',component:HeroDetailComponent}
    
];
