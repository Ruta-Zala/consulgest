import { createRouter, createWebHistory } from 'vue-router';

import LoginPage from './pages/login.page.vue';
import OnboardingPage from './pages/onboarding/index.page.vue';

import DefaultLayout from './layouts/default.layout.vue';
import DashboardLayout from './layouts/dashboard.layout.vue';
import DashboardPage from './pages/dashboard/index.page.vue';
import DashboardDetailPage from './pages/dashboard/detail.page.vue';
import DashboardClosuresPage from './pages/dashboard/closures.page.vue';
import DashboardUrgentCasesPage from './pages/dashboard/urgent-cases.page.vue';

import LotPage from './pages/lots/[lotId].page.vue';

import ConfigurationLayout from './layouts/configuration.layout.vue';
import ConfigurationSystemPage from './pages/configuration/system.page.vue';
import ConfigurationPreferencesPage from './pages/configuration/preferences.page.vue';
import ConfigurationPermissionsPage from './pages/configuration/permissions.page.vue';
import ConfigurationPaymentsPage from './pages/configuration/payments.page.vue';

import DossiersLayout from './layouts/dossiers.layout.vue';
import DossiersPage from './pages/dossiers/index.page.vue';
import DossiersOverviewPage from './pages/dossiers/[dossierId]/index.page.vue';
import DossiersDetailPage from './pages/dossiers/[dossierId]/detail.page.vue';
import DossiersIndividualsPage from './pages/dossiers/[dossierId]/individuals.page.vue';
import DossiersAddressBook from './pages/dossiers/[dossierId]/address-book.page.vue';

import ConsulLayout from './layouts/consul.layout.vue';
import ConsulPage from './pages/consul/index.page.vue';
import ConsulBehaviouralPage from './pages/consul/behavioural.page.vue';

import TeamLayout from './layouts/team.layout.vue';
import TeamPage from './pages/team/index.page.vue';
import TeamUserPage from './pages/team/[user]/index.page.vue';
import TeamPreferencesPage from './pages/team/[user]/preferences.page.vue';
import TeamPasswordPage from './pages/team/[user]/password.page.vue';

import ImportDossierLayout from './layouts/import-dossier.layout.vue';
import ImportDossierPage from './pages/import-dossier/index.page.vue';
import ImportDossierHistoryPage from './pages/import-dossier/history.page.vue';

export const router = createRouter({
	history: createWebHistory(),
	routes: [
		{ path: '/', component: LoginPage },
		{ path: '/onboarding', component: OnboardingPage },
		{
			path: '/',
			component: DefaultLayout,
			children: [
				{
					path: '/dashboard',
					component: DashboardLayout,
					children: [
						// TODO: We are showing `DashboardPage` and `DashboardDetailsPage` on different routes
						// But later this will be only one route.
						// `DashboardPage` is showed when there are no data
						// `DashboardDetailsPage` is showed when we already have some data imported
						{ path: '', component: DashboardPage },
						{ path: 'detail', component: DashboardDetailPage },
						{ path: 'closures', component: DashboardClosuresPage },
						{ path: 'urgent-cases', component: DashboardUrgentCasesPage },
					],
				},
				{
					path: 'lots',
					// TODO: Lots should have their own layout
					component: DashboardLayout,
					children: [{ path: ':lot', component: LotPage }],
				},
				{
					path: 'configuration',
					component: ConfigurationLayout,
					children: [
						{ path: '', component: ConfigurationSystemPage },
						{ path: 'system', component: ConfigurationSystemPage },
						{ path: 'preferences', component: ConfigurationPreferencesPage },
						{ path: 'permissions', component: ConfigurationPermissionsPage },
						{ path: 'payments', component: ConfigurationPaymentsPage },
					],
				},
				{
					path: 'dossiers',
					component: DossiersLayout,
					children: [
						{ path: '', component: DossiersPage, name: 'dossiers' },
						{
							path: ':dossierId',
							props: true,
							children: [
								{
									path: 'overview',
									name: 'dossiers-overview',
									component: DossiersOverviewPage,
								},
								{
									path: 'details',
									name: 'dossiers-details',
									component: DossiersDetailPage,
								},
								{
									path: 'individuals',
									name: 'dossiers-individuals',
									component: DossiersIndividualsPage,
								},
								{
									path: 'address-book',
									name: 'dossiers-address-book',
									component: DossiersAddressBook,
								},
							],
						},
					],
				},
				{
					path: 'consul',
					component: ConsulLayout,
					children: [
						{ path: '', component: ConsulPage },
						{ path: 'behavioural', component: ConsulBehaviouralPage },
					],
				},
				{
					path: 'team',
					component: TeamLayout,
					children: [
						{ path: '', component: TeamPage },
						{ path: 'user', component: TeamUserPage },
						{ path: 'preferences', component: TeamPreferencesPage },
						{ path: 'password', component: TeamPasswordPage },
					],
				},
				{
					path: 'import-dossier',
					component: ImportDossierLayout,
					children: [
						{ path: '', component: ImportDossierPage },
						{ path: 'history-logs', component: ImportDossierHistoryPage },
					],
				},
			],
		},
	],
});
